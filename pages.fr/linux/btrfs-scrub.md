# btrfs scrub

> Éxaminer un système de fichiers btrfs pour vérifier l'intégrité de ses données.
> Il est recommandé de faire tourner une vérification tous les mois.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Démarrer un examen :

`sudo btrfs {{[sc|scrub]}} start {{chemin/vers/point_de_montage_btrfs}}`

- Afficher le statut d'un examen en cours, ou du dernier examen complété :

`sudo btrfs {{[sc|scrub]}} status {{chemin/vers/point_de_montage_btrfs}}`

- Stopper un examen en cours :

`sudo btrfs {{[sc|scrub]}} {{[c|cancel]}} {{chemin/vers/point_de_montage_btrfs}}`

- Reprendre un examen précédemment stoppé :

`sudo btrfs {{[sc|scrub]}} {{[r|resume]}} {{chemin/vers/point_de_montage_btrfs}}`

- Démarrer un examen, mais attendre qu'il termine avant de rendre la main :

`sudo btrfs {{[sc|scrub]}} start -B {{chemin/vers/point_de_montage_btrfs}}`

- Démarrer un examen en mode silencieux (n'affiche ni erreurs ni statistiques) :

`sudo btrfs {{[sc|scrub]}} start {{[-q|--quiet]}} {{chemin/vers/le/point_de_montage_btrfs}}`
