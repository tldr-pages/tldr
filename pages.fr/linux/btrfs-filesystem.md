# btrfs filesystem

> Gérer les systèmes de fichiers BTRFS.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-filesystem>.

- Afficher l'utilisation du système de fichier (affiche les informations détaillées si executé en tant que `root`) :

`btrfs filesystem usage {{path/to/btrfs_mount}}`

- Affichier l'utilisation individuellement pour chaque device :

`sudo btrfs filesystem show {{path/to/btrfs_mount}}`

- Défragmenter un fichier unique sur un système de fichier BTRFS (à éviter lorsque un agent de dé-duplication est en cours d'exécution) :

`sudo btrfs filesystem defragment -v {{path/to/file}}`

- Défragementer récurisivement un répertoire (ne franchit pas la limite de sous-volume) :

`sudo btrfs filesystem defragment -v -r {{path/to/directory}}`

- Force la resynchronisation des blocs de donné non écrit sur le ou les disques :

`sudo btrfs filesystem sync {{path/to/btrfs_mount}}`

- Affiche un sommaire d'utilisation des disques pour les fichiers dans un répertoire, récursivement :

`sudo btrfs filesystem du --summarize {{path/to/directory}}`
