# btrfs subvolume

> Gestion des sous-volumes et instantanés btrfs.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Créer un nouveau sous-volume vide :

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{chemin/vers/nouveau_sous_volume}}`

- Lister tous les sous-volumes et instantanés du système de fichiers indiqué :

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{chemin/vers/systeme_de_fichiers_btrfs}}`

- Supprimer un sous-volume :

`sudo btrfs {{[su|subvolume]}} {{[d|delete]}} {{chemin/vers/sous_volume}}`

- Créer un instantané en lecture seule d'un sous-volume existant :

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} -r {{chemin/vers/sous_volume_source}} {{chemin/vers/sous_volume_cible}}`

- Créer un instantané en lecture et écriture d'un sous-volume existant :

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} {{chemin/vers/sous_volume_source}} {{chemin/vers/sous_volume_cible}}`

- Afficher les informations détaillées d'un sous-volume :

`sudo btrfs {{[su|subvolume]}} {{[sh|show]}} {{chemin/vers/sous_volume}}`
