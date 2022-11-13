# btrfs rescue

> Essayer de récupérer un système de fichiers btrfs endommagé.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- Reconstruire les méta-données du système de fichiers (très lent) :

`sudo btrfs rescue chunk-recover {{chemin/vers/partition}}`

- Corriger les problèmes d'alignement de taille de périphérique (e.g. incohérence entre la taille du système de fichiers et le nombre total d'octets empéchant de monter la partition) :

`sudo btrfs rescue fix-device-size {{chemin/vers/partition}}`

- Restaurer un superbloc corrompu depuis ses copies correctes (restauration de la racine de l'arbre du système de fichiers) :

`sudo btrfs rescue super-recover {{chemin/vers/partition}}`

- Restaurer depuis des transactions interrompues (correction des problèmes de re-exécution des messages de journaux) :

`sudo btrfs rescue zero-log {{chemin/vers/partition}}`

- Créer un périphérique de contrôle sous `/dev/btrfs-control` quand l'outil `mknod` n'est pas installé :

`sudo btrfs rescue create-control-device`
