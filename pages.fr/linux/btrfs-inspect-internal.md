# btrfs inspect-internal

> Recherche des informations internes concernant un système de fichier BTRFS.
> Plus d'information : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-inspect-internal>.

- Afficher les informations du superbloc :

`sudo btrfs inspect-internal dump-super {{chemin/vers/la/partition}}`

- Afficher les informations sur les superblocs et toutes ses copies :

`sudo btrfs inspect-internal dump-super --all {{chemin/vers/la/partition}}`

- Afficher les informations de metadata du système de fichier :

`sudo btrfs inspect-internal dump-tree {{chemin/vers/la/partition}}`

- Afficher la liste des fichiers dans le `n`-ième inode :

`sudo btrfs inspect-internal inode-resolve {{n}} {{chemin/vers/le/point/de/montage/btrfs}}`

- Afficher la liste des fichiers à une adresse logique donnée :

`sudo btrfs inspect-internal logical-resolve {{addresse_logique}} {{chemin/vers/le/point/de/montage/btrfs}}`

- Afficher les statistiques concernant les arbres de racines, de domaines (*extent*), de checksum (*csum*) et de système de fichier :

`sudo btrfs inspect-internal tree-stats {{chemin/vers/la/partition}}`
