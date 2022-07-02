# top

> Mostra informació dinàmica en temps real sobre processos executant-se.
> Més informació: <https://manned.org/top>.

- Inicia top:

`top`

- No mostra cap procés inactiu o zombie:

`top -i`

- Mostra només processos pertanyents a un usari donat:

`top -u {{usuari}}`

- Ordena processos per una columna:

`top -o {{nom_columna}}`

- Mostra els fils individuals d'un procés donat:

`top -Hp {{id_procés}}`

- Mostra només els processos amb un(s) PID(s) donat(s), separats per comes. (Normalment no es coneix el PID amb antelació. Aquest exemple l'obté del nom del procés):

`top -p $(pgrep -d ',' {{nom_procés}})`

- Obté ajuda sobre els commandaments interactius:

`?`
