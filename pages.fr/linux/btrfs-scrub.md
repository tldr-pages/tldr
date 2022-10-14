# btrfs scrub

> Examiner un système de fichier BTRFS pour vérifier l'integrité des données.
> Il est recommandé de faire tourner une vérification tout les mois.
> Plus d'informations : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-scrub>.

- Démarrer un examen :

`sudo btrfs scrub start {{chemin/vers/le/point/de/montage/btrfs}}`

- Afficher le statut d'un examen en cours, ou du dernier examen complété :

`sudo btrfs scrub status {{chemin/vers/le/point/de/montage/btrfs}}`

- Stopper un examen en cours :

`sudo btrfs scrub cancel {{chemin/vers/le/point/de/montage/btrfs}}`

- Reprendre un examen précedemment stoppé :

`sudo btrfs scrub resume {{chemin/vers/le/point/de/montage/btrfs}}`

- Démarrer un examen, mais attendre qu'il termine avant de rendre la main :

`sudo btrfs scrub start -B {{chemin/vers/le/point/de/montage/btrfs}}`

- Démarrer un examen en mode silencieux (n'affiche ni erreurs ni statistiques) :

`sudo btrfs scrub start -q {{chemin/vers/le/point/de/montage/btrfs}}`
