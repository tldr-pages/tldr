# btrfs filesystem

> Gérer les systèmes de fichiers btrfs.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- Afficher l'utilisation du système de fichiers (affiche les informations détaillées si executé en tant que `root`) :

`btrfs filesystem usage {{chemin/vers/point_de_montage_btrfs}}`

- Afficher l'utilisation individuellement pour chaque périphérique :

`sudo btrfs filesystem show {{chemin/vers/point_de_montage_btrfs}}`

- Défragmenter un fichier unique sur un système de fichiers btrfs (à éviter lorsqu'un agent de dé-duplication est en cours d'exécution) :

`sudo btrfs filesystem defragment -v {{chemin/vers/fichier}}`

- Défragmenter récursivement un dossier (ne franchit pas la limite de sous-volume) :

`sudo btrfs filesystem defragment -v -r {{chemin/vers/dossier}}`

- Force la resynchronisation des blocs de données non écrits sur le ou les disques :

`sudo btrfs filesystem sync {{chemin/vers/point_de_montage_btrfs}}`

- Afficher un sommaire d'utilisation des disques pour les fichiers dans un dossier, récursivement :

`sudo btrfs filesystem du --summarize {{chemin/vers/dossier}}`
