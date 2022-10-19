# btrfs device

> Gestion des partitions dans un système de fichiers BTRFS.
> Plus d'information : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-device>.

- Ajouter un ou plusieurs périphériques à un système de fichiers btrfs :

`sudo btrfs device add {{chemin/vers/block_device1}} [{{chemin/vers/block_device2}}] {{chemin/vers/systeme_de_fichiers_btrfs}}`

- Retirer un périphérique d'un système de fichiers btrfs :

`sudo btrfs device remove {{chemin/vers/peripherique|identifiant_peripherique}} [{{...}}]`

- Afficher les statistiques d'erreurs :

`sudo btrfs device stats {{chemin/vers/systeme_de_fichiers_btrfs}}`

- Scanner tout les disques et informer le noyaux de tout les sytèmes de fichiers BTRFS détectés :

`sudo btrfs device scan --all-devices`

- Affichier les statistiques détaillées d'allocation par disque :

`sudo btrfs device usage {{chemin/vers/systeme_de_fichier_btrfs}}`
