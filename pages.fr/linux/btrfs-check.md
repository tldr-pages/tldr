# btrfs check

> Vérifier l'état, ou réparer un système de fichier de type BTRFS.
> Plus d'informations : <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-check>.

- Vérifier l'état d'un système de fichier btrfs :

`sudo btrfs check {{path/to/partition}}`

- Vérifier l'état et réparer d'un système de fichier btrfs (dangereux) :

`sudo btrfs check --repair {{path/to/partition}}`

- Afficher la progression de vérification en cours :

`sudo btrfs check --progress {{path/to/partition}}`

- Vérifier la somme de contrôle (*checksum*) de chaque bloc de donné (si le système de fichier à été correctement vérifié) :

`sudo btrfs check --check-data-csum {{path/to/partition}}`

- Utiliser le `n`-ième super-bloc (`n` peut-être `0`, `1` ou `2`) :

`sudo btrfs check --super {{n}} {{path/to/partition}}`

- Reconstruire l'arbre des sommes de contrôle (*checksum tree*) :

`sudo btrfs check --repair --init-csum-tree {{path/to/partition}}`

- Reconstruire l'arbre des domaines (*extent*) :

`sudo btrfs check --repair --init-extent-tree {{path/to/partition}}`
