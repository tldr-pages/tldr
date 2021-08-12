# ps

> Informații despre procesele care rulează.

- Listează toate procesele care rulează:

`ps aux`

- Listează toate procesele care rulează, inclusiv șirul de comandă complet:

`ps auxww`

- Căutați un proces care se potrivește cu un șir:

`ps aux | grep {{string}}`

- Listează toate procesele utilizatorului curent în format complet suplimentar:

`ps --user $(id -u) -F`

- Listează toate procesele utilizatorului curent ca arbore:

`ps --user $(id -u) f`

- Ia pid părinte a unui proces:

`ps -o ppid= -p {{pid}}`

- Sortarea proceselor după consumul de memorie:

`ps --sort size`
