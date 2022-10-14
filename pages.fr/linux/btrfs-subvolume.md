# btrfs subvolume

> Gestion des sous-volumes et snapshots BTRFS.
> Plus d'information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-subvolume>.

- Créer un nouve sous-volume vide :

`sudo btrfs subvolume create {{chemin/vers/nouveau_subvolume}}`

- Lister tout les sous-volumes et snapshots du système de fichier indiqué :

`sudo btrfs subvolume list {{chemin/vers/btrfs_filesystem}}`

- Supprimer un sous-volume :

`sudo btrfs subvolume delete {{path/to/subvolume}}`

- Créer un snapshot en lecture seule d'un sous-volume existant :

`sudo btrfs subvolume snapshot -r {{path/to/source_subvolume}} {{path/to/target}}`

- Créer un snapshot en lecture et écriture d'un sous-volume existant :

`sudo btrfs subvolume snapshot {{path/to/source_subvolume}} {{path/to/target}}`

- Afficher les informations détaillées d'un sous-volume :

`sudo btrfs subvolume show {{path/to/subvolume}}`
