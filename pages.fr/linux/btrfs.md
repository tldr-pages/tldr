# btrfs

> Système de fichiers basé sur le principe de copie à l’écriture ("copy-on-write", souvent désigné par son sigle anglais COW) pour Linux.
> Certaines sous-commandes comme `btrfs device` ont leur propre documentation.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Créer un sous-volume :

`sudo btrfs subvolume create {{chemin/vers/sous_volume}}`

- Lister les sous-volumes :

`sudo btrfs subvolume list {{chemin/vers/point_de_montage}}`

- Afficher les informations d'utilisation d'espace :

`sudo btrfs filesystem df {{chemin/vers/point_de_montage}}`

- Activer les quotas :

`sudo btrfs quota enable {{chemin/vers/sous_volume}}`

- Afficher les quotas :

`sudo btrfs qgroup show {{chemin/vers/sous_volume}}`
