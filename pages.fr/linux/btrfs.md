# btrfs

> Système de fichier basé sur le principe de copie à l’écriture ("copy-on-write", souvent désigné par son sigle anglais COW) pour Linux.
> Certaines sous-commandes comme `btrfs device` ont leur propre documentation.
> Plus d'informations : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

- Créer un sous-volume :

`sudo btrfs subvolume create {{path/to/subvolume}}`

- Lister les sous-volumes:

`sudo btrfs subvolume list {{path/to/mount_point}}`

- Afficher les informations d'utilisation d'espace :

`sudo btrfs filesystem df {{path/to/mount_point}}`

- Activater les quotas :

`sudo btrfs quota enable {{path/to/subvolume}}`

- Afficher les quotas :

`sudo btrfs qgroup show {{path/to/subvolume}}`
