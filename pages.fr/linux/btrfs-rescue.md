# btrfs rescue

> Essayer de récupérer un système de fichier BTRFS endommagé.
> Plus d'informations: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-rescue>.

- Reconstruire les méta-data du système de fichier (très lent) :

`sudo btrfs rescue chunk-recover {{chemin/vers/partition}}`

- Corriger les problèmes d'alignement de taille de device (e.g. incohérence entre la taille du système de fichiers et le nombre total d'octets empéchant de monter la partition) :

`sudo btrfs rescue fix-device-size {{chemin/vers/partition}}`

- Restaurer un superbloc corrompu depuis ses copies correct (restauration de la racine de l'arbre du système de fichiers) :

`sudo btrfs rescue super-recover {{chemin/vers/partition}}`

- Restaurer depuis des transactions interrompues (correction des problème de ré-exection des messages de log):

`sudo btrfs rescue zero-log {{chemin/vers/partition}}`

- Créer un device de contrôle sous `/dev/btrfs-control` quand l'outil `mknod` n'est pas installé :

`sudo btrfs rescue create-control-device`
