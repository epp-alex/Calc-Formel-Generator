# Référence des fonctions – Assistant de formules LibreOffice Calc

Toutes les fonctions disponibles dans le programme, avec syntaxe, paramètres et exemples.

---

## Onglet 1 – Fonctions de base

### Opérateurs arithmétiques

| Opérateur | Signification | Exemple | Résultat |
|-----------|---------------|---------|----------|
| `+` | Addition | `=A1+B1` | Somme de deux cellules |
| `-` | Soustraction | `=A1-B1` | Différence |
| `*` | Multiplication | `=A1*B1` | Produit |
| `/` | Division | `=A1/B1` | Quotient |
| `^` | Puissance | `=A1^2` | A1 au carré |

---

### SOMME
**Syntaxe :** `=SOMME(plage)`

Additionne tous les nombres d'une plage de cellules.

| Paramètre | Description |
|-----------|-------------|
| `plage` | p. ex. `A1:A10` |

```
=SOMME(A1:A10)
```

---

### MOYENNE
**Syntaxe :** `=MOYENNE(plage)`

Calcule la moyenne de tous les nombres de la plage.

```
=MOYENNE(A1:A10)
```

---

### MIN
**Syntaxe :** `=MIN(plage)`

Renvoie la valeur la plus petite de la plage.

```
=MIN(A1:A10)
```

---

### MAX
**Syntaxe :** `=MAX(plage)`

Renvoie la valeur la plus grande de la plage.

```
=MAX(A1:A10)
```

---

### NB
**Syntaxe :** `=NB(plage)`

Compte toutes les cellules contenant des **valeurs numériques** dans la plage.

```
=NB(A1:A10)
```

---

### NBVAL
**Syntaxe :** `=NBVAL(plage)`

Compte toutes les cellules **non vides** (nombres et texte).

```
=NBVAL(A1:A10)
```

---

### MEDIANE
**Syntaxe :** `=MEDIANE(plage)`

Renvoie la valeur centrale de la liste de valeurs triées.

```
=MEDIANE(A1:A10)
```

---

### SOMMEPROD
**Syntaxe :** `=SOMMEPROD(plage1; plage2)`

Multiplie les éléments de deux plages entre eux et additionne les résultats.

| Paramètre | Description |
|-----------|-------------|
| `plage1` | Première plage |
| `plage2` | Deuxième plage (même taille) |

```
=SOMMEPROD(A1:A10; B1:B10)
```

---

## Onglet 2 – Fonctions avancées

### SI
**Syntaxe :** `=SI(condition; alors; sinon)`

Renvoie l'une de deux valeurs selon que la condition est vraie ou fausse.

| Paramètre | Description |
|-----------|-------------|
| `condition` | p. ex. `A1>0` |
| `alors` | Valeur si vrai |
| `sinon` | Valeur si faux |

```
=SI(A1>0; "OK"; "Erreur")
```

---

### ET
**Syntaxe :** `=ET(condition1; condition2)`

Renvoie VRAI si **toutes** les conditions sont remplies.

```
=ET(A1>0; B1>0)
```

---

### OU
**Syntaxe :** `=OU(condition1; condition2)`

Renvoie VRAI si **au moins une** condition est remplie.

```
=OU(A1>0; B1>0)
```

---

### NON
**Syntaxe :** `=NON(condition)`

Inverse une valeur logique : VRAI → FAUX, FAUX → VRAI.

```
=NON(A1>0)
```

---

### SOMME.SI
**Syntaxe :** `=SOMME.SI(plage; critère; plage_somme)`

Additionne les valeurs qui correspondent à un critère.

| Paramètre | Description |
|-----------|-------------|
| `plage` | Plage évaluée |
| `critère` | p. ex. `">10"` ou `"Oui"` |
| `plage_somme` | Plage à additionner |

```
=SOMME.SI(A1:A10; ">10"; B1:B10)
```

---

### NB.SI
**Syntaxe :** `=NB.SI(plage; critère)`

Compte les cellules qui correspondent à un critère.

```
=NB.SI(A1:A10; "Oui")
```

---

### MOYENNE.SI
**Syntaxe :** `=MOYENNE.SI(plage; critère; plage_moyenne)`

Calcule la moyenne des valeurs qui correspondent à un critère.

```
=MOYENNE.SI(A1:A10; ">0"; B1:B10)
```

---

### SOMME.SI.ENS
**Syntaxe :** `=SOMME.SI.ENS(plage_somme; plage_critères; critère)`

Additionne les valeurs qui correspondent à **plusieurs** critères.

| Paramètre | Description |
|-----------|-------------|
| `plage_somme` | Plage à additionner |
| `plage_critères` | Plage évaluée |
| `critère` | Condition, p. ex. `">10"` |

```
=SOMME.SI.ENS(A1:A10; B1:B10; ">10")
```

---

### ECARTYPE
**Syntaxe :** `=ECARTYPE(plage)`

Calcule l'écart type (dispersion des valeurs).

```
=ECARTYPE(A1:A10)
```

---

### VAR
**Syntaxe :** `=VAR(plage)`

Calcule la variance (dispersion au carré).

```
=VAR(A1:A10)
```

---

### NB.VIDE
**Syntaxe :** `=NB.VIDE(plage)`

Compte toutes les cellules **vides** de la plage.

```
=NB.VIDE(A1:A10)
```

---

### GRANDE.VALEUR
**Syntaxe :** `=GRANDE.VALEUR(plage; k)`

Renvoie la k-ième plus grande valeur de la plage.

| Paramètre | Description |
|-----------|-------------|
| `plage` | Plage de nombres |
| `k` | Rang (1 = plus grande, 2 = deuxième plus grande, …) |

```
=GRANDE.VALEUR(A1:A10; 2)
```

---

## Onglet 3 – Date et texte

### AUJOURD'HUI
**Syntaxe :** `=AUJOURD'HUI()`

Renvoie la date du jour. Se met à jour à chaque ouverture du fichier.

```
=AUJOURD'HUI()
```

---

### MAINTENANT
**Syntaxe :** `=MAINTENANT()`

Renvoie la date du jour **avec l'heure**.

```
=MAINTENANT()
```

---

### ANNEE
**Syntaxe :** `=ANNEE(date)`

Extrait l'année d'une date.

```
=ANNEE(A1)
```

---

### MOIS
**Syntaxe :** `=MOIS(date)`

Extrait le mois (1–12) d'une date.

```
=MOIS(A1)
```

---

### JOUR
**Syntaxe :** `=JOUR(date)`

Extrait le jour (1–31) d'une date.

```
=JOUR(A1)
```

---

### DATE
**Syntaxe :** `=DATE(année; mois; jour)`

Crée une date à partir de valeurs individuelles.

```
=DATE(2025; 1; 1)
```

---

### DATEDIF
**Syntaxe :** `=DATEDIF(date_début; date_fin; unité)`

Calcule la différence entre deux dates.

| Unité | Signification |
|-------|---------------|
| `"D"` | Jours |
| `"M"` | Mois |
| `"Y"` | Années |

```
=DATEDIF(A1; B1; "D")
```

> **Remarque :** DATEDIF est une fonction non documentée – elle fonctionne dans LibreOffice et Excel, mais n'apparaît pas dans la saisie automatique.

---

### JOURSEM
**Syntaxe :** `=JOURSEM(date; type)`

Renvoie le jour de la semaine sous forme de nombre.

| Type | Signification |
|------|---------------|
| `2` | 1=Lun, 2=Mar, … 7=Dim (recommandé) |
| `1` | 1=Dim, 2=Lun, … 7=Sam |

```
=JOURSEM(A1; 2)
```

---

### CONCATENER
**Syntaxe :** `=CONCATENER(texte1; texte2; …)`

Assemble plusieurs textes en un seul.

```
=CONCATENER(A1; " "; B1)
```

---

### NBCAR
**Syntaxe :** `=NBCAR(texte)`

Renvoie le nombre de caractères d'un texte.

```
=NBCAR(A1)
```

---

### GAUCHE
**Syntaxe :** `=GAUCHE(texte; nombre)`

Renvoie les n premiers caractères d'un texte.

```
=GAUCHE(A1; 5)
```

---

### DROITE
**Syntaxe :** `=DROITE(texte; nombre)`

Renvoie les n derniers caractères d'un texte.

```
=DROITE(A1; 5)
```

---

### STXT
**Syntaxe :** `=STXT(texte; position_départ; nombre)`

Renvoie une portion d'un texte.

| Paramètre | Description |
|-----------|-------------|
| `texte` | Texte source |
| `position_départ` | À partir de quel caractère (1 = premier) |
| `nombre` | Combien de caractères |

```
=STXT(A1; 1; 5)
```

---

### MAJUSCULE
**Syntaxe :** `=MAJUSCULE(texte)`

Convertit toutes les lettres en majuscules.

```
=MAJUSCULE(A1)
```

---

### MINUSCULE
**Syntaxe :** `=MINUSCULE(texte)`

Convertit toutes les lettres en minuscules.

```
=MINUSCULE(A1)
```

---

### SUPPRESPACE
**Syntaxe :** `=SUPPRESPACE(texte)`

Supprime les espaces superflus (en début, en fin et les doublons).

```
=SUPPRESPACE(A1)
```

---

## Onglet 4 – Recherche et arrondis

### RECHERCHEV
**Syntaxe :** `=RECHERCHEV(valeur_cherchée; matrice; index_colonne; correspondance)`

Recherche une valeur dans la **première colonne** d'un tableau et renvoie la valeur d'une autre colonne.

| Paramètre | Description |
|-----------|-------------|
| `valeur_cherchée` | Valeur recherchée, p. ex. `A1` |
| `matrice` | Plage de recherche, p. ex. `B1:D10` |
| `index_colonne` | Numéro de la colonne à renvoyer (1 = première colonne) |
| `correspondance` | `0` = exacte, `1` = approximative |

```
=RECHERCHEV(A1; B1:D10; 2; 0)
```

---

### RECHERCHEH
**Syntaxe :** `=RECHERCHEH(valeur_cherchée; matrice; index_ligne; correspondance)`

Comme RECHERCHEV, mais recherche dans la **première ligne** (horizontalement).

```
=RECHERCHEH(A1; B1:D10; 2; 0)
```

---

### INDEX
**Syntaxe :** `=INDEX(plage; ligne; colonne)`

Renvoie la valeur à une position précise dans la plage.

| Paramètre | Description |
|-----------|-------------|
| `plage` | Plage de recherche |
| `ligne` | Numéro de ligne |
| `colonne` | Numéro de colonne (défaut : 1) |

```
=INDEX(B1:B10; 3; 1)
```

---

### EQUIV
**Syntaxe :** `=EQUIV(valeur_cherchée; plage_recherche; type_correspondance)`

Renvoie la **position** d'une valeur dans une plage.

| Type de correspondance | Signification |
|------------------------|---------------|
| `0` | Correspondance exacte |
| `1` | La plus petite valeur supérieure ou égale |
| `-1` | La plus grande valeur inférieure ou égale |

```
=EQUIV(A1; A1:A10; 0)
```

---

### INDEX + EQUIV
**Syntaxe :** `=INDEX(plage_résultat; EQUIV(valeur_cherchée; plage_recherche; 0))`

Alternative plus flexible à RECHERCHEV – peut rechercher dans **n'importe quelle direction**.

| Paramètre | Description |
|-----------|-------------|
| `plage_résultat` | Colonne contenant les valeurs à renvoyer |
| `valeur_cherchée` | Valeur recherchée |
| `plage_recherche` | Colonne dans laquelle chercher |

```
=INDEX(B1:B10; EQUIV(A1; A1:A10; 0))
```

> **Avantage sur RECHERCHEV :** La colonne de recherche n'a pas besoin d'être la première. Également stable lors de l'insertion ou la suppression de colonnes.

---

### ARRONDI
**Syntaxe :** `=ARRONDI(nombre; décimales)`

Arrondit au nombre de décimales indiqué.

| Décimales | Exemple |
|-----------|---------|
| `2` | 3,14159 → 3,14 |
| `0` | 3,7 → 4 |
| `-1` | 34 → 30 |

```
=ARRONDI(A1; 2)
```

---

### ARRONDI.SUP
**Syntaxe :** `=ARRONDI.SUP(nombre; décimales)`

Arrondit toujours **vers le haut** (en s'éloignant de zéro).

```
=ARRONDI.SUP(A1; 2)
```

---

### ARRONDI.INF
**Syntaxe :** `=ARRONDI.INF(nombre; décimales)`

Arrondit toujours **vers le bas** (vers zéro).

```
=ARRONDI.INF(A1; 2)
```

---

### ENT
**Syntaxe :** `=ENT(nombre)`

Arrondit à l'entier le plus proche **vers le bas** (y compris pour les nombres négatifs).

```
=ENT(A1)
```

---

### TRONQUE
**Syntaxe :** `=TRONQUE(nombre; décimales)`

Supprime les décimales **sans arrondir**.

```
=TRONQUE(A1; 2)
```

---

### ABS
**Syntaxe :** `=ABS(nombre)`

Renvoie la **valeur absolue** (toujours positive).

```
=ABS(A1)
```

---

### MOD
**Syntaxe :** `=MOD(nombre; diviseur)`

Renvoie le **reste** d'une division.

```
=MOD(A1; 3)
```
> Exemple : `=MOD(10; 3)` → `1`

---

### RACINE
**Syntaxe :** `=RACINE(nombre)`

Calcule la racine carrée.

```
=RACINE(A1)
```

---

### ALEA
**Syntaxe :** `=ALEA()`

Renvoie un nombre décimal aléatoire compris entre 0 et 1. Se met à jour à chaque recalcul.

```
=ALEA()
```

> Pour un nombre aléatoire entre 1 et 100 : `=ENT(ALEA()*100)+1`

---

## Références absolues

Dans le programme, le mode de référence peut être sélectionné via un menu déroulant :

| Mode | Exemple | Signification |
|------|---------|---------------|
| Relative | `A1` | Se déplace lors de la copie |
| Colonne fixe | `$A1` | La colonne est fixe, la ligne se déplace |
| Ligne fixe | `A$1` | La ligne est fixe, la colonne se déplace |
| Absolue | `$A$1` | Reste toujours identique lors de la copie |

---

## Raccourcis clavier

| Raccourci | Fonction |
|-----------|----------|
| `Ctrl+S` | Enregistrer la formule dans les favoris |
| `Ctrl+C` | Copier la formule |
| `Ctrl+Z` | Annuler |
| `Ctrl+Y` | Rétablir |
| `Ctrl+F12` | Réduire / restaurer la fenêtre |
| `Suppr` | Supprimer un favori (dans la liste) |
