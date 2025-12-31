# gdb

> Le débogueur GNU.
> Plus d'informations : <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>.

- Débogue un exécutable :

`gdb {{exécutable}}`

- Attache un processus à gdb :

`gdb {{[-p|--pid]}} {{identifiant_processus}}`

- Débogue avec un fichier comme image mémoire :

`gdb {{[-c|--core]}} {{fichier}} {{exécutable}}`

- Execute les commandes gdb données au démarrage :

`gdb {{[-ex|--eval-command]}} "{{commandes}}" {{exécutable}}`

- Démarre gdb en passant des arguments à l'exécutable :

`gdb --args {{exécutable}} {{argument1}} {{argument2}}`
