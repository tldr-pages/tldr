# btrfs filesystem

> Gérer les systèmes de fichiers BTRFS.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-filesystem>.

- Afficher l'utilisation du système de fichier (affiche les informations détaillées si executé en tant que `root`) :

`btrfs filesystem usage {{chemin/vers/point_de_montage_btrfs}}`

- Affichier l'utilisation individuellement pour chaque device :

`sudo btrfs filesystem show {{chemin/vers/point_de_montage_btrfs}}`

- Défragmenter un fichier unique sur un système de fichier BTRFS (à éviter lorsque un agent de dé-duplication est en cours d'exécution) :

`sudo btrfs filesystem defragment -v {{chemin/vers/fichier}}`

- Défragementer récurisivement un répertoire (ne franchit pas la limite de sous-volume) :

`sudo btrfs filesystem defragment -v -r {{chemin/vers/repertoire}}`

- Force la resynchronisation des blocs de donné non écrit sur le ou les disques :

`sudo btrfs filesystem sync {{chemin/vers/point_de_montage_btrfs}}`

- Affiche un sommaire d'utilisation des disques pour les fichiers dans un répertoire, récursivement :

`sudo btrfs filesystem du --summarize {{chemin/vers/repertoire}}`
