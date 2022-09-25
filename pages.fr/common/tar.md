# tar

> Utilitaire d'archivage.
> Souvent combiné avec une méthode de compression, telle que gzip ou bzip2.
> Plus d'informations : <https://www.gnu.org/software/tar>.

- Crée une archive à partir de fichiers :

`tar cf {{cible.tar}} {{fichier1 fichier2 fichier3}}`

- Crée une archive gzip :

`tar czf {{cible.tar.gz}} {{fichier1 fichier2 fichier3}}`

- Extrait une archive (compressée) dans le dossier courant :

`tar xf {{source.tar[.gz|.bz2|.xz]}}`

- Extrait une archive dans un dossier cible :

`tar xf {{source.tar}} -C {{dossier}}`

- Crée une archive compressée, en utilisant le suffixe de l'archive pour déterminer le programme de compression :

`tar caf {{cible.tar.xz}} {{fichier1 fichier2 fichier3}}`

- Liste le contenu d'une archive tar :

`tar tvf {{source.tar}}`

- Extrait les fichiers correspondant au motif :

`tar xf {{source.tar}} --wildcards "{{*.html}}"`
