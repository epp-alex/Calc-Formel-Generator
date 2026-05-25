# LibreOffice Calc Assistant de Formules

Un outil Python pour créer, tester et gérer rapidement des formules LibreOffice Calc – avec système de favoris, synchronisation d'équipe, multilinguisme et gestionnaire de plugins.

## 🚀 Fonctionnalités

- 📑 4 onglets avec plus de 60 fonctions

- 🌐 38 langues (dont le hindi avec installation automatique de police)

- ⭐ Système de favoris (local et synchronisation d'équipe via lecteur réseau)

- 🛠 Panneau d'administration pour les favoris d'équipe (protégé par mot de passe)

- 📋 Formules directement copiables avec coloration syntaxique

- ✏️ Champ de sortie modifiable avec Annuler/Rétablir

- 📖 Aide intégrée et référence des fonctions (par langue)

- 💾 Sauvegarde automatique (JSON, écriture atomique)

- 🌙 Mode sombre

- 🔌 Gestionnaire de plugins pour créer ses propres plugins de formules

- 🔤 Prise en charge RTL (droite vers gauche) – détection automatique du sens d'écriture

- 🗄️ Sauvegarde et restauration – enregistrez tous les paramètres et favoris avec un nom et un mot de passe

- ⌨️ Raccourci global `Ctrl+F12` pour réduire/restaurer
- 🔍 Validateur JSON – vérification et correction automatiques de `languages.json` et `formula_explanations.json`

## 🖥️ Utilisation

**1. Saisir les données**

- Plage de cellules (ex. `A1:A10`)

- Cellule 1 / Cellule 2 (ex. `A1`, `B1`)

- Paramètre optionnel (ex. texte ou index)

- Mode de référence absolue sélectionnable : `A1`, `$A1`, `A$1`, `$A$1`

**2. Sélectionner une fonction** Choisissez un onglet et cliquez sur une fonction – la formule est générée instantanément.

**3. Ajuster la formule** La formule générée peut être modifiée directement dans le champ de sortie.

**4. Copier** En un clic dans le presse-papiers (couleurs syntaxiques incluses).

**5. Utiliser les favoris**

- ⭐ Enregistrer → sauvegarder la formule actuelle (Ctrl+S)

- 📂 Charger → réutiliser une formule

- ❌ Supprimer → touche Suppr ou bouton

- 🕐 Historique → formules récemment utilisées

## 📊 Aperçu des onglets

**Onglet 1 – Fonctions de base** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Onglet 2 – Fonctions avancées** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Onglet 3 – Date et texte** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Onglet 4 – Recherche et arrondi** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Explications des formules depuis la documentation LibreOffice

Le fichier `formula_explanations.json` est alimenté directement depuis la **documentation officielle de LibreOffice Calc** (https://help.libreoffice.org).

### Source de données et mise à jour

- Les descriptions, les informations de syntaxe et les exemples sont tirés du site d'aide officiel de LibreOffice
- Les langues prises en charge dépendent des traductions disponibles sur le site
- Le fichier contient pour chaque fonction : nom, syntaxe, description, exemple et catégorie
- Des ajouts ou corrections peuvent être effectués manuellement (voir Validateur JSON)

### Structure de `formula_explanations.json`

```json
{
  "SUM": {
    "fr": {
      "syntax": "SUM(Nombre1; Nombre2; ...)",
      "description": "Additionne tous les nombres d'une plage de cellules.",
      "example": "=SUM(A1:A10)"
    },
    "en": {
      "syntax": "SUM(Number1; Number2; ...)",
      "description": "Adds all numbers in a cell range.",
      "example": "=SUM(A1:A10)"
    }
  }
}
```

| Champ | Obligatoire | Description |
|-------|------------|-------------|
| `syntax` | ✅ | Syntaxe de la formule avec paramètres |
| `description` | ✅ | Courte description de la fonction |
| `example` | ✅ | Exemple d'utilisation comme formule prête à l'emploi |
| `note` | ❌ | Note optionnelle |

> 💡 **Remarque :** Si aucune entrée n'existe pour une langue, l'application revient automatiquement à la version anglaise.

---

## 🔍 Validateur JSON pour les fichiers de langue

Le **Validateur JSON** intégré vérifie et corrige `languages.json` et `formula_explanations.json` en termes de cohérence, d'exhaustivité et de désignations de pays correctes.

Accessible via **Paramètres → 🔍 Validateur JSON**.

### Que vérifie-t-on ?

#### `languages.json`

- ✅ Les 38 langues sont présentes (par code ISO 639-1)
- ✅ **Noms de pays et de langues corrects** (ex. `"fr"` → `"Français"`)
- ✅ Aucun code de langue en double
- ✅ Champs obligatoires présents : `name`, `native_name`, `flag`, `rtl`
- ✅ Indicateur RTL correctement défini (Arabe, Hébreu, Persan, Ourdou → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Toutes les fonctions des 4 onglets sont enregistrées
- ✅ Champs obligatoires présents : `syntax`, `description`, `example`
- ✅ Aucun champ vide (`""` ou `null`)
- ✅ Les codes de langue correspondent à `languages.json`

### Fonctions de correction

| Type d'erreur | Correction automatique |
|--------------|----------------------|
| Nom de pays incorrect | Remplacé par le nom correct selon la norme ISO |
| Entrée de langue manquante | Complété avec une version de secours en anglais |
| Champ obligatoire vide | Marqué comme `"[MISSING]"` pour révision manuelle |
| Entrée dupliquée | Doublons supprimés, l'entrée la plus complète est conservée |
| Indicateur RTL incorrect | Corrigé automatiquement selon les codes RTL connus |

### Mode d'emploi

1. Ouvrir **Paramètres → 🔍 Validateur JSON**
2. Sélectionner le fichier : `languages.json` ou `formula_explanations.json` (ou les deux)
3. **🔎 Vérifier** – affiche tous les problèmes détectés
4. **🛠 Corriger automatiquement** – résout toutes les erreurs corrigibles automatiquement
5. **💾 Enregistrer** – écrit le fichier corrigé de manière atomique
6. **📋 Exporter le rapport** (optionnel) – enregistre un fichier texte avec tous les résultats

> ⚠️ **Remarque :** Avant toute correction automatique, une copie de sauvegarde du fichier original est créée (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Système de favoris

- Enregistrer et réutiliser ses propres formules

- Séparation entre favoris personnels et favoris d'équipe

- Les favoris d'équipe sont en lecture seule (seul l'administrateur peut les modifier)

- Les doublons sont évités

- Tri libre des favoris personnels

- Synchronisation via lecteur réseau (configurable en option)

### Synchronisation d'équipe

Via **Paramètres → 🌐 Chemin réseau**, il est possible de renseigner un lecteur réseau (ex. `\\\\Serveur\\Partage\\formules`).

- Au démarrage : les favoris réseau sont sauvegardés localement (copie hors ligne)

- À l'enregistrement : les formules personnelles sont écrites sur le réseau, les formules d'équipe ne sont pas touchées

## 🛠 Panneau d'administration

Accessible via le bouton 🛠. Au premier clic, un mot de passe est défini (PBKDF2-SHA256, seul le hachage est enregistré).

- Ajouter, modifier et supprimer des formules d'équipe

- Changer le mot de passe

- Les modifications sont écrites directement sur le lecteur réseau

## 🔌 Gestionnaire de plugins

Le gestionnaire de plugins (`plugin_manager.py`) est un outil autonome pour créer et gérer ses propres plugins de formules pour Calc2. Il se trouve dans le même dossier que `Calc2.py` et est lancé via le bouton 🔌 dans Calc2.py :

### Fonctions

- **Créer un nouveau plugin** – assistant pas à pas (nom, formules, traductions, résumé)

- **Ajouter des formules** – compléter un plugin existant avec de nouvelles formules

- **Modifier les traductions** – traduire les noms de formules dans les 38 langues

- **Ouvrir le dossier des plugins** – directement dans l'explorateur de fichiers

- **Supprimer un plugin** – avec confirmation de sécurité

### Structure d'un plugin

Chaque plugin se trouve en tant que sous-dossier dans `plugins/` et est composé de deux fichiers :

```
plugins/
  mon_plugin/
    plugin.json      ← métadonnées (nom, version, auteur, description)
    formulas.json    ← formules avec traductions
```

**Exemple `plugin.json` :**

```
{
  "id": "mon_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "Votre Nom",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "fr": "Formules Financières" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**Exemple `formulas.json` :**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "fr": "Somme de la plage" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "fr": "Basique" }
  }
]
```

### Avis important (⚠️ Important Notice)

Dans le gestionnaire de plugins se trouve le bouton **⚠️ Important Notice**. Un clic ouvre une fenêtre avec toutes les règles de création correcte de plugins en anglais. Les mêmes informations sont également disponibles dans `IMPORTANT_NOTICE.md`.

## 🌐 Multilinguisme

38 langues disponibles, commutables directement dans l'application.
De nouvelles langues peuvent être ajoutées via le bouton 🌍 avec l'assistant de langue.

**Remarque sur le hindi (हिंदी) :** Lors du premier passage en hindi, la police *Noto Sans Devanagari* est installée une seule fois au niveau du système. Windows demandera des droits d'administrateur.

## 🔤 Prise en charge RTL (droite vers gauche)

Les langues à écriture de droite à gauche sont détectées automatiquement et toute l'interface est mise en miroir :

- **Arabe (عربي)** – détection RTL automatique
- **Hébreu (עברית)** – détection RTL automatique
- **Persan / Farsi (فارسی)** – détection RTL automatique
- **Ourdou (اردو)** – détection RTL automatique

**Ce qui change en mode RTL :** La disposition complète de l'interface est inversée, les champs de saisie utilisent l'alignement RTL, la police bascule automatiquement vers une police compatible RTL (ex. *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Remarque :** Les formules LibreOffice générées restent toujours en syntaxe LTR – seule l'interface change de sens.


## 🗄️ Sauvegarde et restauration

### Créer une sauvegarde

Via **Paramètres → 🗄️ Créer une sauvegarde** :

1. **Nom** – librement choisi (ex. `Sauvegarde_Mai_2025`)
2. **Mot de passe** – la sauvegarde est chiffrée AES ; sans le mot de passe, aucune restauration n'est possible
3. **Emplacement** – local ou sur un lecteur réseau
4. Cliquez sur **💾 Créer une sauvegarde** – un fichier `.calc2backup` est créé

**Contenu :** Tous les favoris, paramètres, favoris d'équipe (optionnel), plugins installés.

### Restaurer une sauvegarde

Via **Paramètres → 📂 Restaurer une sauvegarde** :

1. Sélectionnez le fichier (`.calc2backup`)
2. Saisissez le mot de passe
3. Choisissez la portée : favoris uniquement / paramètres uniquement / tout
4. Cliquez sur **🔄 Restaurer**

> ⚠️ Les données existantes sont écrasées lors de la restauration. Une sauvegarde automatique des données actuelles est proposée au préalable.


## 💡 Conseils

- `$A$1` → référence absolue (liste déroulante à côté des champs de cellule)

- **Ctrl+S** → enregistrer la formule dans les favoris

- **Ctrl+C** → copier la formule (en dehors des champs de saisie)

- **Ctrl+Z / Ctrl+Y** → Annuler / Rétablir

- **Ctrl+F12** → réduire/restaurer la fenêtre (fonctionne même lorsque Calc2 est réduit)

- **Touche Suppr** dans la liste des favoris → supprimer une entrée

- Les formules peuvent être ajustées directement dans le champ de sortie après génération

## 📁 Structure du projet

```
Calc2.py                        ← programme principal
plugin_manager.py               ← gestionnaire de plugins
IMPORTANT_NOTICE.md             ← instructions pour la création de plugins
data/
  README_fr.md / README_en.md / ...      ← aide par langue
  REFERENCE_fr.md / REFERENCE_en.md / ... ← référence des fonctions par langue
language/
  languages.json                ← traductions de l'interface (38 langues)
  formula_explanations.json
services/
  language_tool.py              ← assistant : ajouter une nouvelle langue
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← sauvegarde et restauration
  json_validator.py             ← vérification et correction de languages.json / formula_explanations.json
plugins/                        ← dossier des plugins (créé automatiquement)
  mon_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← police hindi
  NotoSansArabic-Regular.ttf      ← police arabe (RTL)
  NotoSansHebrew-Regular.ttf      ← police hébraïque (RTL)
python/                         ← Python intégré
  python.exe
  ...
settings.json                   ← créé automatiquement
favoris.json                    ← favoris locaux (créé automatiquement)
```

## 🧠 Points techniques notables

- **Écriture atomique des fichiers** → évite la corruption des fichiers lors de la sauvegarde

- **Architecture orientée services** → logique et interface utilisateur strictement séparées

- **Migration automatique** → les anciens formats de favoris sont détectés et convertis

- **Gestion robuste des erreurs** → les fichiers corrompus ne provoquent pas de plantage

- **Coloration syntaxique** → les formules sont affichées en couleur

- **Mode sombre** → entièrement pris en charge

- **Système de plugins** → Calc2 est extensible via des plugins de formules personnalisés

- **Moteur RTL** → détection automatique des langues RTL, mise en miroir complète de l'interface avec les polices adaptées

- **Sauvegarde et restauration** → sauvegardes chiffrées AES avec nom et mot de passe, restauration sélective

- **Validateur JSON** → vérification et correction automatiques de `languages.json` et `formula_explanations.json` incl. noms de pays et champs obligatoires

- **Source LibreOffice** → `formula_explanations.json` est alimenté depuis la documentation officielle de LibreOffice Calc (https://help.libreoffice.org)

- **Raccourci global** → `Ctrl+F12` fonctionne au niveau du système via la bibliothèque `keyboard` (thread en arrière-plan)

## Licence

Utilisation libre à des fins personnelles et commerciales.
