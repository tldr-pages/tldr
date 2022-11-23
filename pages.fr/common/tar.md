# tar

> Utilitaire d'archivage.
> Souvent combiné avec une méthode de compression, telle que gzip ou bzip2.
> Plus d'informations : <https://www.gnu.org/software/tar>.

- Crée une archive à partir de fichiers :

`tar cf {{cible.tar}} {{fichier1}} {{fichier2}} {{fichier3}}`

- Crée une archive gzip à partir de fichiers :

`tar czf {{cible.tar.gz}} {{fichier1}} {{fichier2}} {{fichier3}}`

- Crée une archive gzip à partir d'un répertoire en utilisant son chemin relatif :

`tar czf {{target.tar.gz}} --directory={{chemin/vers/répertoire}} .`

- Extrait une archive (compressée) dans le dossier courant en affichant la liste des fichiers traités :

`tar xvf {{source.tar[.gz|.bz2|.xz]}}`

- Extrait une archive (compressée) dans un répertoire cible :

`tar xf {{source.tar[.gz|.bz2|.xz]}} --directory={{répertoire}}`

- Crée une archive compressée, en utilisant le suffixe de l'archive pour déterminer le programme de compression :

`tar caf {{cible.tar.xz}} {{fichier1}} {{fichier2}} {{fichier3}}`

- Liste les fichiers contenus dans une archive tar :

`tar tvf {{source.tar}}`

- Extrait les fichiers correspondant au motif :

`tar xf {{source.tar}} --wildcards "{{*.html}}"`
