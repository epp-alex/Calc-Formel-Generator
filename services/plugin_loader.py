#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plugin Loader Service  –  v1.0.1 (Fix: formula als Dict unterstützt)
"""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Tuple

logger = logging.getLogger("calc2.plugin_loader")


def _resolve_text(obj: Any, lang: str, fallback: str = "en") -> str:
    if obj is None:
        return ""
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        if lang in obj:
            return obj[lang]
        if fallback in obj and fallback != lang:
            return obj[fallback]
        for v in obj.values():
            if isinstance(v, str):
                return v
    return ""


def _resolve_formula(obj: Any, lang: str, fallback: str = "en") -> str:
    """
    Wie _resolve_text, aber speziell für das formula-Feld.
    Unterstützt sowohl einfache Strings als auch mehrsprachige Dicts:
      "=SUMME(A1:A10)"
      {"en": "=SUM(A1:A10)", "de": "=SUMME(A1:A10)", ...}
    """
    if obj is None:
        return ""
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        # Bevorzuge die gewünschte Sprache
        if lang in obj:
            return obj[lang]
        # Fallback-Sprache
        if fallback in obj:
            return obj[fallback]
        # Englisch als letzten Ausweg
        if "en" in obj:
            return obj["en"]
        # Erster vorhandener String-Wert
        for v in obj.values():
            if isinstance(v, str):
                return v
    return ""


def _version_tuple(version_str: str) -> tuple:
    try:
        return tuple(int(x) for x in str(version_str).split("."))
    except (ValueError, AttributeError):
        return (0,)


def _check_min_version(plugin_min: str, app_version: str) -> bool:
    if not plugin_min:
        return True
    return _version_tuple(app_version) >= _version_tuple(plugin_min)


@dataclass
class FormulaEntry:
    formula:     str
    name:        str
    description: str
    category:    str
    raw:         dict = field(default_factory=dict, repr=False)


@dataclass
class PluginData:
    id:          str
    name:        str
    description: str
    version:     str
    author:      str
    icon:        str
    enabled:     bool
    formulas:    List[FormulaEntry] = field(default_factory=list)
    plugin_dir:  Path = field(default=None, repr=False)
    raw_meta:    dict = field(default_factory=dict, repr=False)
    raw_formulas: List[dict] = field(default_factory=list, repr=False)


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        logger.debug("JSON nicht gefunden: %s", path)
        return None
    except json.JSONDecodeError as e:
        logger.warning("JSON-Fehler in %s: %s", path, e)
        return None
    except Exception as e:
        logger.error("Fehler beim Lesen von %s: %s", path, e)
        return None


def _load_formulas(
    formulas_path: Path,
    lang: str,
    fallback: str,
) -> Tuple[List[FormulaEntry], List[dict]]:
    raw_list = _load_json(formulas_path)
    if not isinstance(raw_list, list):
        return [], []

    entries = []
    for i, item in enumerate(raw_list):
        if not isinstance(item, dict):
            logger.warning("formulas.json Eintrag %d ist kein Dict – übersprungen", i)
            continue

        # FIX: formula kann ein String ODER ein mehrsprachiges Dict sein
        formula_raw = item.get("formula", "")
        formula_str = _resolve_formula(formula_raw, lang, fallback)

        if not formula_str:
            logger.warning("formulas.json Eintrag %d hat keine 'formula' – übersprungen", i)
            continue

        entries.append(FormulaEntry(
            formula     = formula_str,
            name        = _resolve_text(item.get("name"),        lang, fallback) or formula_str,
            description = _resolve_text(item.get("description"), lang, fallback),
            category    = _resolve_text(item.get("category"),    lang, fallback),
            raw         = item,
        ))

    return entries, raw_list


def _load_single_plugin(
    plugin_dir:  Path,
    lang:        str,
    fallback:    str,
    app_version: str,
) -> "PluginData | None":
    plugin_json = plugin_dir / "plugin.json"
    if not plugin_json.exists():
        logger.debug("Kein plugin.json in %s – übersprungen", plugin_dir)
        return None

    meta = _load_json(plugin_json)
    if not isinstance(meta, dict):
        logger.warning("plugin.json in %s ist ungültig – übersprungen", plugin_dir)
        return None

    if not meta.get("enabled", True):
        logger.info("Plugin '%s' ist deaktiviert – übersprungen", plugin_dir.name)
        return None

    min_ver = meta.get("min_app_version", "")
    if not _check_min_version(min_ver, app_version):
        logger.warning(
            "Plugin '%s' benötigt App-Version %s (aktuell %s) – übersprungen",
            plugin_dir.name, min_ver, app_version,
        )
        return None

    name_raw = meta.get("name")
    name = _resolve_text(name_raw, lang, fallback)
    if not name:
        logger.warning("Plugin '%s' hat keinen 'name' – übersprungen", plugin_dir.name)
        return None

    formulas_path = plugin_dir / "formulas.json"
    formulas, raw_formulas = _load_formulas(formulas_path, lang, fallback)

    plugin = PluginData(
        id           = plugin_dir.name,
        name         = name,
        description  = _resolve_text(meta.get("description"), lang, fallback),
        version      = str(meta.get("version", "1.0")),
        author       = str(meta.get("author", "")),
        icon         = str(meta.get("icon", "")),
        enabled      = True,
        formulas     = formulas,
        plugin_dir   = plugin_dir,
        raw_meta     = meta,
        raw_formulas = raw_formulas,
    )

    logger.info(
        "Plugin geladen: '%s' v%s (%d Formeln)",
        plugin.name, plugin.version, len(plugin.formulas),
    )
    return plugin


def get_plugin_text(obj: Any, lang: str, fallback_lang: str = "en") -> str:
    return _resolve_text(obj, lang, fallback_lang)


def resolve_formulas(
    raw_formulas: List[dict],
    lang:         str,
    fallback:     str = "en",
) -> List[FormulaEntry]:
    """Löst raw_formulas bei Sprachumschaltung neu auf."""
    entries = []
    for item in raw_formulas:
        if not isinstance(item, dict):
            continue

        # FIX: formula kann ein String ODER ein mehrsprachiges Dict sein
        formula_raw = item.get("formula", "")
        formula_str = _resolve_formula(formula_raw, lang, fallback)

        if not formula_str:
            continue

        entries.append(FormulaEntry(
            formula     = formula_str,
            name        = _resolve_text(item.get("name"),        lang, fallback) or formula_str,
            description = _resolve_text(item.get("description"), lang, fallback),
            category    = _resolve_text(item.get("category"),    lang, fallback),
            raw         = item,
        ))
    return entries


def load_all_plugins(
    plugins_dir:   Path,
    lang:          str,
    fallback_lang: str = "en",
    app_version:   str = "1.0.0",
) -> List[PluginData]:
    if not plugins_dir.exists():
        logger.info("plugins/-Ordner nicht gefunden: %s", plugins_dir)
        return []

    if not plugins_dir.is_dir():
        logger.warning("plugins/-Pfad ist kein Ordner: %s", plugins_dir)
        return []

    loaded = []
    for entry in sorted(plugins_dir.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name.startswith("_") or entry.name.startswith("."):
            continue

        plugin = _load_single_plugin(entry, lang, fallback_lang, app_version)
        if plugin is not None:
            loaded.append(plugin)

    logger.info("Plugin-Loader: %d Plugin(s) geladen aus %s", len(loaded), plugins_dir)
    return loaded