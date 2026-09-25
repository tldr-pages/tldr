# btrfs device

> Gestion des partitions dans un système de fichiers BTRFS.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Ajoute un ou plusieurs périphériques à un système de fichiers btrfs :

`sudo btrfs {{[d|device]}} {{[a|add]}} {{chemin/vers/block_device1 chemin/vers/block_device2 ...}} {{chemin/vers/systeme_de_fichiers_btrfs}}`

- Retire un périphérique d'un système de fichiers btrfs :

`sudo btrfs {{[d|device]}} {{[rem|remove]}} {{chemin/vers/peripherique1|identifiant_peripherique1 chemin/vers/peripherique2|identifiant_peripherique2 ...}}`

- Affiche les statistiques d'erreurs :

`sudo btrfs {{[d|device]}} {{[st|stats]}} {{chemin/vers/systeme_de_fichiers_btrfs}}`

- Scanne tous les disques et informer le noyau de tous les sytèmes de fichiers btrfs détectés :

`sudo btrfs {{[d|device]}} {{[sc|scan]}} {{[-d|--all-devices]}}`

- Affiche les statistiques détaillées d'allocation par disque :

`sudo btrfs {{[d|device]}} {{[u|usage]}} {{chemin/vers/systeme_de_fichiers_btrfs}}`
