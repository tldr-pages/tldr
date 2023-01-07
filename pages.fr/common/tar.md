# tar

> Utilitaire d'archivage.
> Souvent combiné avec une méthode de compression, telle que gzip ou bzip2.
> Plus d'informations : <https://www.gnu.org/software/tar>.

- Crée une archive à partir de fichiers :

`tar cf {{chemin/vers/cible.tar}} {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Crée une archive gzip à partir de fichiers :

`tar czf {{chemin/vers/cible.tar.gz}} {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Crée une archive gzip à partir d'un répertoire en utilisant son chemin relatif :

`tar czf {{chemin/vers/cible.tar.gz}} --directory={{chemin/vers/répertoire}} .`

- Extrait une archive (compressée) dans le dossier courant en affichant la liste des fichiers traités :

`tar xvf {{chemin/vers/source.tar[.gz|.bz2|.xz]}}`

- Extrait une archive (compressée) dans un répertoire cible :

`tar xf {{chemin/vers/source.tar[.gz|.bz2|.xz]}} --directory={{répertoire}}`

- Crée une archive compressée, en utilisant le suffixe de l'archive pour déterminer le programme de compression :

`tar caf {{chemin/vers/cible.tar.xz}} {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Liste les fichiers contenus dans une archive tar :

`tar tvf {{chemin/vers/source.tar}}`

- Extrait les fichiers correspondant au motif :

`tar xf {{source.tar}} --wildcards "{{*.html}}"`
