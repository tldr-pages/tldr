# rsync

> Transférer des fichiers vers ou depuis un hôte distant (pas entre deux hôtes distants).
> Peut transférer un ou plusieurs fichiers correspondant à un motif.
> Plus d'informations : <https://download.samba.org/pub/rsync/rsync.1>.

- Transférer un fichier local vers un serveur distant :

`rsync {{chemin/vers/fichier_local}} {{hote_distant}}:{{chemin/vers/dossier_distant}}`

- Transférer un fichier d'un serveur distant vers l'hôte local :

`rsync {{hote_distant}}:{{chemin/vers/fichier_distant}} {{chemin/vers/dossier_local}}`

- Transférer un fichier sous forme d'[a]rchive (pour conserver les attributs) et compressé ([z]ippé), en mode [v]erbeux, lisible par l'[h]umain et afficher la [p]rogression du transfert :

`rsync -azvhP {{chemin/vers/fichier_local}} {{hote_distant}}:{{chemin/vers/dossier_distant}}`

- Transférer un dossier et tous ses sous-dossiers d'un hôte distant vers l'hôte local :

`rsync -r {{hote_distant}}:{{chemin/vers/dossier_distant}} {{chemin/vers/dossier_local}}`

- Transférer le contenu d'un dossier (mais pas le dossier lui-même) d'un hôte distant vers un hôte local :

`rsync -r {{hote_distant}}:{{chemin/vers/dossier_distant}}/ {{chemin/vers/dossier_local}}`

- Transférer un dossier [r]écursivement, dans une [a]rchive pour conserver les attributs, en résolvant les [l]iens symboliques, et ignorant les fichiers déjà transférés sa[u]f si plus récents :

`rsync -rauL {{hote_distant}}:{{chemin/vers/fichier_distant}} {{chemin/vers/dossier_local}}`

- Transférer un fichier par SSH et effacer les fichiers de l'hôte local qui n'existent pas sur l'hôte distant :

`rsync -e ssh --delete {{hote_distant}}:{{chemin/vers/fichier_distant}} {{chemin/vers/fichier_local}}`

- Transférer un fichier par SSH et afficher l'avancement global du transfert :

`rsync -e ssh --info=progress2 {{hote_distant}}:{{chemin/vers/fichier_distant}} {{chemin/vers/fichier_local}}`
