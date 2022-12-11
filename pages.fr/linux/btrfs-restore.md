# btrfs restore

> Tenter de récupérer des fichiers depuis un système de fichiers btrfs endommagé.
> Plus d'information : <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restaurer tout les fichiers depuis un système de fichier btrfs vers un répertoire cible indiqué :

`sudo btrfs restore {{chemin/vers/peripherique_btrfs}} {{chemin/vers/dossier}}`

- Lister (sans écriture) les fichiers qui peuvent être récupérés depuis un système de fichiers btrfs :

`sudo btrfs restore --dry-run {{chemin/du/device/btrfs}} {{chemin/du/dossier}}`

- Restaurer les fichiers correspondants à une expression régulière donnée (non sensible à la casse) à restaurer depuis un système de fichiers btrfs (tous les répertoires parents des fichiers doivent correspondre également à l'expression régulière) :

`sudo btrfs restore --path-regex {{expression_reguliere}} -c {{chemin/vers/peripherique_btrfs}} {{chemin/vers/dossier}}`

- Restaurer les fichiers depuis un système de fichiers btrfs en utilisant un arbre racine spécifique `bytenr` (voir `btrfs-find-root`) :

`sudo btrfs restore -t {{bytenr}} {{chemin/vers/peripherique_btrfs}} {{chemin/vers/dossier}}`

- Restaurer les fichiers depuis un système de fichiers btrfs (avec métadonnées, attributs étendus, et liens symboliques) en écrivant par dessus les fichiers déjà existants dans le répertoire cible :

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{chemin/vers/peripherique_btrfs}} {{chemin/vers/dossier}}`
