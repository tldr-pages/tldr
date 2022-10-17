# btrfs subvolume

> Gestion des sous-volumes et snapshots BTRFS.
> Plus d'information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-subvolume>.

- Créer un nouve sous-volume vide :

`sudo btrfs subvolume create {{chemin/vers/nouveau_sousvolume}}`

- Lister tout les sous-volumes et snapshots du système de fichier indiqué :

`sudo btrfs subvolume list {{chemin/vers/btrfs_filesystem}}`

- Supprimer un sous-volume :

`sudo btrfs subvolume delete {{chemin/vers/sousvolume}}`

- Créer un snapshot en lecture seule d'un sous-volume existant :

`sudo btrfs subvolume snapshot -r {{chemin/vers/sousvolume_source}} {{chemin/vers/cible}}`

- Créer un snapshot en lecture et écriture d'un sous-volume existant :

`sudo btrfs subvolume snapshot {{chemin/vers/sousvolume_source}} {{chemin/vers/cible}}`

- Afficher les informations détaillées d'un sous-volume :

`sudo btrfs subvolume show {{chemin/vers/sousvolume}}`
