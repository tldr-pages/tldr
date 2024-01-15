# rsync

> Transférer des fichiers vers ou depuis un hôte distant (pas entre deux hôtes distants).
> Peut transférer un ou plusieurs fichiers correspondant à un motif.
> Plus d'informations : <https://download.samba.org/pub/rsync/rsync.1>.

- Transfère un fichier :

`rsync {{chemin/vers/origine}} {{chemin/vers/destination}}`

- Utilise le mode archive (copier récursivement les répertoires, copier les liens symboliques sans résolution et conserver les autorisations, la propriété et les délais de modification) :

`rsync --archive {{chemin/vers/origine}} {{chemin/vers/destination}}`

- Transférer le contenu d'un dossier :

`rsync --recursive {{chemin/vers/origine}} {{chemin/vers/destination}}`

- Transférer le contenu d'un dossier (mais pas le dossier lui-même) :

`rsync --recursive {{chemin/vers/origine}}/ {{chemin/vers/destination}}`

- Utiliser le mode archive, résolvant les liens symboliques et ignorant les fichiers déjà transférés sauf si plus récents :

`rsync --archive --update --copy-links {{chemin/vers/origine}} {{chemin/vers/destination}}`

- Transférer un fichier vers un hôte distant exécutant `rsyncd` et supprimez les fichiers sur la destination qui n'existent pas sur l'hôte distant :

`rsync --recursive --delete rsync://{{hote_distant}}:{{chemin/vers/origine}} {{chemin/vers/destination}}`

- Transférer un fichier par SSH et afficher l'avancement global du transfert :

`rsync -rsh 'ssh -p {{port}}' --info=progress2 {{hote_distant}}:{{chemin/vers/origine}} {{chemin/vers/destination}}`
