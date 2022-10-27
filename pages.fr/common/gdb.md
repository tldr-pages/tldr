# gdb

> Le débogueur GNU.
> Plus d'informations : <https://www.gnu.org/software/gdb>.

- Débogue un exécutable :

`gdb {{exécutable}}`

- Attache un processus à gdb :

`gdb -p {{identifiant_processus}}`

- Débogue avec un fichier comme image mémoire :

`gdb -c {{fichier}} {{exécutable}}`

- Execute les commandes gdb données au démarrage :

`gdb -ex "{{commandes}}" {{exécutable}}`

- Démarre gdb en passant des arguments à l'exécutable :

`gdb --args {{exécutable}} {{argument1}} {{argument2}}`
