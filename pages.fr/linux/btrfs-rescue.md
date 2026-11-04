# btrfs rescue

> Essaie de récupérer un système de fichiers btrfs endommagé.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- Reconstruit les méta-données du système de fichiers (très lent) :

`sudo btrfs {{[resc|rescue]}} {{[ch|chunk-recover]}} {{chemin/vers/partition}}`

- Corrige les problèmes d'alignement de taille de périphérique (e.g. incohérence entre la taille du système de fichiers et le nombre total d'octets empéchant de monter la partition) :

`sudo btrfs {{[resc|rescue]}} {{[fix-de|fix-device-size]}} {{chemin/vers/partition}}`

- Restaure un superbloc corrompu depuis ses copies correctes (restauration de la racine de l'arbre du système de fichiers) :

`sudo btrfs {{[resc|rescue]}} {{[s|super-recover]}} {{chemin/vers/partition}}`

- Restaure depuis des transactions interrompues (correction des problèmes de re-exécution des messages de journaux) :

`sudo btrfs {{[resc|rescue]}} {{[z|zero-log]}} {{chemin/vers/partition}}`

- Crée un périphérique de contrôle sous `/dev/btrfs-control` quand l'outil `mknod` n'est pas installé :

`sudo btrfs {{[resc|rescue]}} {{[c|create-control-device]}}`
