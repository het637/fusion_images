
# Fusion d'Images

Ce projet implémente une technique de fusion d'images en utilisant la manipulation des bits des pixels pour cacher une image dans une autre. Le programme fonctionne en intégrant les bits les plus significatifs d'une image secrète dans les bits les moins significatifs d'une image visible.

## Fonctionnalités
- Charge deux images (`image1.jpg` et `cecieestuneimage.jpg`)
- Convertit les pixels en représentation binaire
- Manipule les bits des pixels pour encoder une image dans une autre
- Génère une image fusionnée (`image_fusion.jpg`)

## Prérequis
Ce programme nécessite `Python` et la bibliothèque `Pillow` (PIL) pour fonctionner.

Installez les dépendances avec :
```bash
pip install pillow
```

## Utilisation
Placez vos images dans le même dossier que le script et assurez-vous qu'elles sont nommées :
- `image1.jpg` : l'image visible
- `cecieestuneimage.jpg` : l'image cachée

Puis exécutez le script :
```bash
python fusion.py
```
L'image résultante `image_fusion.jpg` sera générée et affichée.

## Explication Technique
1. **Conversion en binaire** : Chaque pixel des images est converti en sa représentation binaire (8 bits par canal RGB).
2. **Suppression des bits faibles** : Les 4 bits de poids faible de l'image visible sont mis à zéro.
3. **Déplacement des bits forts** : Les 4 bits de poids fort de l'image cachée sont déplacés vers les 4 bits de poids faible.
4. **Fusion des images** : Les pixels transformés sont combinés et reconstruits pour créer l'image finale.



