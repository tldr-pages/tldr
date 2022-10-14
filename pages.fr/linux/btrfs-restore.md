# btrfs restore

> Tenter de récupérer des fichiers depuis un système de fichiers BTRFS endommagé.
> Plus d'information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-restore>.

- Restaurer tout les fichiers depuis un système de fichier BTRFS vers un répertoire cible indiqué :

`sudo btrfs restore {{chemin/du/device/btrfs}} {{chemin/du/repertoire}}`

- Lister (sans écriture) les fichiers qui peuvent être récupérés depuis un système de fichiers BTRFS :

`sudo btrfs restore --dry-run {{chemin/du/device/btrfs}} {{chemin/du/repertoire}}`

- Restaurer les fichiers correspondant à une regex donnée (non sensible à la casse) à restaurer depuis un système de fichiers BTRFS (tout les répertoires parents des fichiers doivent correspondre à la regex également) :

`sudo btrfs restore --path-regex {{regex}} -c {{chemin/du/device/btrfs}} {{chemin/du/repertoire}}`

- Restaurer les fichiers depuis un système de fichiers BTRFS en utilisant un arbre racine spécifique `bytenr` (voir `btrfs-find-root`) :

`sudo btrfs restore -t {{bytenr}} {{chemin/du/device/btrfs}} {{chemin/du/repertoire}}`

- Restaurer les fichiers depuis un système de fichiers BTRFS (avec métadata, attributs étendus, et liens symboliques), en écrivant par dessus les fichiers déjà existant dans le répertoire cible:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{chemin/du/device/btrfs}} {{chemin/du/repertoire}}`
