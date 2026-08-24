# btrfs inspect-internal

> Recherche des informations internes concernant un système de fichier btrfs.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- Afficher les informations du superbloc :

`sudo btrfs {{[i|inspect-internal]}} {{[dump-s|dump-super]}} {{chemin/vers/partition}}`

- Afficher les informations sur les superblocs et toutes ses copies :

`sudo btrfs {{[i|inspect-internal]}} {{[dump-s|dump-super]}} {{[-a|--all]}} {{chemin/vers/partition}}`

- Afficher les meta-informations du système de fichiers :

`sudo btrfs {{[i|inspect-internal]}} {{[dump-t|dump-tree]}} {{chemin/vers/partition}}`

- Afficher la liste des fichiers dans le `n`-ième inode :

`sudo btrfs {{[i|inspect-internal]}} {{[i|inode-resolve]}} {{n}} {{chemin/vers/point_de_montage_btrfs}}`

- Afficher la liste des fichiers à une adresse logique donnée :

`sudo btrfs {{[i|inspect-internal]}} {{[lo|logical-resolve]}} {{addresse_logique}} {{chemin/vers/point_de_montage_btrfs}}`

- Afficher les statistiques concernant les arbres de racines, de domaines (extent), de sommes de contrôle (csum) et de système de fichiers :

`sudo btrfs {{[i|inspect-internal]}} {{[t|tree-stats]}} {{chemin/vers/partition}}`
