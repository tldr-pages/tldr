# btrfs check

> Vérifier l'état, ou réparer un système de fichiers de type btrfs.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Vérifier l'état d'un système de fichiers btrfs :

`sudo btrfs {{[c|check]}} {{chemin/vers/partition}}`

- Vérifier l'état et réparer d'un système de fichiers btrfs (dangereux) :

`sudo btrfs {{[c|check]}} --repair {{chemin/vers/partition}}`

- Afficher la progression de vérification en cours :

`sudo btrfs {{[c|check]}} {{[-p|--progress]}} {{chemin/vers/partition}}`

- Vérifier la somme de contrôle de chaque bloc de données (si le système de fichiers à été correctement vérifié) :

`sudo btrfs {{[c|check]}} --check-data-csum {{chemin/vers/partition}}`

- Utiliser le `n`-ième super-bloc (`n` peut-être `0`, `1` ou `2`) :

`sudo btrfs {{[c|check]}} {{[-s|--super]}} {{n}} {{chemin/vers/partition}}`

- Reconstruire l'arbre des sommes de contrôle (checksum tree) :

`sudo btrfs {{[c|check]}} --repair --init-csum-tree {{chemin/vers/partition}}`

- Reconstruire l'arbre des domaines (extent tree) :

`sudo btrfs {{[c|check]}} --repair --init-extent-tree {{chemin/vers/partition}}`
