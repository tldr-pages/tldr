# btrfs

> Un système de fichiers pour Linux basé sur le principe "copy-on-write" (COW).
> Certaines commandes comme `btrfs device` ont leur propre documentation.
> Plus d'informations : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

- Crée un sous-volume :

`sudo btrfs subvolume create {{chemin/vers/le/sous-volume}}`

- Liste les sous-volumes :

`sudo btrfs subvolume list {{chemin/vers/le/point/de/montage}}`

- Affiche les informations d'utilisation de l'espace :

`sudo btrfs filesystem df {{chemin/vers/le/point/de/montage}}`

- Active le quota :

`sudo btrfs quote enable {{chemin/vers/le/sous-volume}}`

- Affiche le quota :

`sudo btrfs qgroup show {{chemin/vers/le/sous-volume}}`
