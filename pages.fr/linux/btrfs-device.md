# btrfs device

> Gestion des partitions dans un système de fichiers BTRFS.
> Plus d'information : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-device>.

- Ajouter un ou plusieurs devices à un système de fichier BTRFS :

`sudo btrfs device add {{path/to/block_device1}} [{{path/to/block_device2}}] {{path/to/btrfs_filesystem}}`

- Retirer un device d'un système de ficheir BTRFS :

`sudo btrfs device remove {{path/to/device|device_id}} [{{...}}]`

- Afficher les statistiques d'erreurs :

`sudo btrfs device stats {{path/to/btrfs_filesystem}}`

- Scanner tout les disques et informer le noyaux de tout les sytèmes de fichiers BTRFS détectés :

`sudo btrfs device scan --all-devices`

- Affichier les statistiques détaillées d'allocation par disque :

`sudo btrfs device usage {{path/to/btrfs_filesystem}}`
