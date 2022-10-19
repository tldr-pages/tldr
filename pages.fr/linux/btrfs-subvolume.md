# btrfs subvolume

> Gestion des sous-volumes et instantanés btrfs.
> Plus d'information : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-subvolume>.

- Créer un nouveau sous-volume vide :

`sudo btrfs subvolume create {{chemin/vers/nouveau_sous_volume}}`

- Lister tous les sous-volumes et instantanés du système de fichiers indiqué :

`sudo btrfs subvolume list {{chemin/vers/systeme_de_fichiers_btrfs}}`

- Supprimer un sous-volume :

`sudo btrfs subvolume delete {{chemin/vers/sous_volume}}`

- Créer un instantané en lecture seule d'un sous-volume existant :

`sudo btrfs subvolume snapshot -r {{chemin/vers/sous_volume_source}} {{chemin/vers/sous_volume_cible}}`

- Créer un instantané en lecture et écriture d'un sous-volume existant :

`sudo btrfs subvolume snapshot {{chemin/vers/sous_volume_source}} {{chemin/vers/sous_volume_cible}}`

- Afficher les informations détaillées d'un sous-volume :

`sudo btrfs subvolume show {{chemin/vers/sous_volume}}`
