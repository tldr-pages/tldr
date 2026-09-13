# btrfs restore

> Tente de récupérer des fichiers depuis un système de fichiers btrfs endommagé.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restaure tous les fichiers depuis un système de fichier btrfs vers un répertoire cible indiqué :

`sudo btrfs {{[rest|restore]}} {{chemin/vers/peripherique_btrfs}} {{chemin/vers/repertoire}}`

- Liste (sans écriture) les fichiers qui peuvent être récupérés depuis un système de fichiers btrfs :

`sudo btrfs {{[rest|restore]}} {{[-D|--dry-run]}} {{chemin/vers/peripherique_btrfs}} {{chemin/vers/repertoire}}`

- Restaure les fichiers correspondants à une `regex` donnée (non sensible à la casse) à restaurer depuis un système de fichiers btrfs (tous les répertoires parents des fichiers doivent correspondre également à la `regex`) :

`sudo btrfs {{[rest|restore]}} --path-regex {{regex}} -c {{chemin/vers/peripherique_btrfs}} {{chemin/vers/repertoire}}`

- Restaure les fichiers depuis un système de fichiers btrfs en utilisant un arbre racine spécifique `bytenr` (voir `btrfs-find-root`) :

`sudo btrfs {{[rest|restore]}} -t {{bytenr}} {{chemin/vers/peripherique_btrfs}} {{chemin/vers/repertoire}}`

- Restaure les fichiers depuis un système de fichiers btrfs (avec métadonnées, attributs étendus, et liens symboliques) en écrivant par dessus les fichiers déjà existants dans le répertoire cible :

`sudo btrfs {{[rest|restore]}} {{[-m|--metadata]}} {{[-x|--xattr]}} {{[-S|--symlinks]}} {{[-o|--overwrite]}} {{chemin/vers/peripherique_btrfs}} {{chemin/vers/repertoire}}`
