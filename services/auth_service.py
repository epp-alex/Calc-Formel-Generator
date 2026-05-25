"""
services/auth_service.py
~~~~~~~~~~~~~~~~~~~~~~~~~
Admin-Authentifizierung mit PBKDF2-HMAC-SHA256.
Kein PyQt5-Import – vollständig UI-unabhängig.
"""
import hashlib
from typing import Optional, Tuple
import json
import secrets

from .settings_service import ADMIN_FILE, Config, atomic_write, log_exc

HASH_ITERATIONS = Config.HASH_ITERATIONS


# ---------------------------------------------------------------------------
# Passwort-Hashing
# ---------------------------------------------------------------------------
def _hash_password(password: str, salt: Optional[bytes] = None) -> Tuple[str, str]:
    """Gibt (salt_hex, hash_hex) zurück."""
    if salt is None:
        salt = secrets.token_bytes(32)
    dk = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, HASH_ITERATIONS
    )
    return salt.hex(), dk.hex()


def _verify_password(password: str, salt_hex: str, hash_hex: str) -> bool:
    """Vergleicht das Passwort mit dem gespeicherten Hash."""
    # Wandle den Hex-Salt zurück in Bytes um
    salt = bytes.fromhex(salt_hex)
    
    # Berechne den Hash des eingegebenen Passworts mit demselben Salt
    # Nutze dafür die bereits vorhandene _hash_password Funktion
    _, new_hash = _hash_password(password, salt)
    
    # Nutze secrets.compare_digest für einen zeitkonstanten Vergleich
    # Dies verhindert sogenannte Timing-Attacks.
    return secrets.compare_digest(new_hash, hash_hex)


# ---------------------------------------------------------------------------
# Admin-Config  (lokal – admin.json enthält nur Hash + Salt, nie Klartext)
# ---------------------------------------------------------------------------
def load_admin_config() -> dict:
    """Gibt {'salt': ..., 'hash': ...} zurück, oder {} wenn kein Passwort gesetzt."""
    if ADMIN_FILE.exists():
        try:
            return json.loads(ADMIN_FILE.read_text(encoding="utf-8"))
        except Exception as e:
            log_exc("Konnte admin.json nicht lesen", e)
    return {}


def save_admin_config(cfg: dict) -> None:
    atomic_write(ADMIN_FILE, json.dumps(cfg, indent=2))


def admin_password_is_set() -> bool:
    cfg = load_admin_config()
    return bool(cfg.get("salt") and cfg.get("hash"))


def check_admin_password(password: str) -> bool:
    cfg = load_admin_config()
    if not cfg.get("salt") or not cfg.get("hash"):
        return False
    return _verify_password(password, cfg["salt"], cfg["hash"])


def set_admin_password(new_password: str) -> None:
    salt, hsh = _hash_password(new_password)
    save_admin_config({"salt": salt, "hash": hsh})
