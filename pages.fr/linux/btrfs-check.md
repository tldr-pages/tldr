# btrfs check

> Vérifier l'état, ou réparer un système de fichiers de type btrfs.
> Plus d'informations : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-check>.

- Vérifier l'état d'un système de fichiers btrfs :

`sudo btrfs check {{chemin/vers/partition}}`

- Vérifier l'état et réparer d'un système de fichiers btrfs (dangereux) :

`sudo btrfs check --repair {{chemin/vers/partition}}`

- Afficher la progression de vérification en cours :

`sudo btrfs check --progress {{chemin/vers/partition}}`

- Vérifier la somme de contrôle de chaque bloc de données (si le système de fichiers à été correctement vérifié) :

`sudo btrfs check --check-data-csum {{chemin/vers/partition}}`

- Utiliser le `n`-ième super-bloc (`n` peut-être `0`, `1` ou `2`) :

`sudo btrfs check --super {{n}} {{chemin/vers/partition}}`

- Reconstruire l'arbre des sommes de contrôle (checksum tree) :

`sudo btrfs check --repair --init-csum-tree {{chemin/vers/partition}}`

- Reconstruire l'arbre des domaines (extent tree) :

`sudo btrfs check --repair --init-extent-tree {{chemin/vers/partition}}`
