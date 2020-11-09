# tree

> Mostra i contenuti della cartella corrente come un albero.
> Maggiori informazioni: <http://mama.indstate.edu/users/ice/tree/>.

- Stampa file e cartella fino al 'num'-esimo livello di profondità (dove 1 significa la cartella corrente):

`tree -L {{num}}`

- Stampa solamente le cartelle:

`tree -d`

- Stampa anche i file nascosti con la colorazione attiva:

`tree -a -C`

- Stampa l'albero senza linee di indentazione, mostrando invece il percorso completo (usa `-N` per non convertire caratteri non stampabili in sequenze di escape):

`tree -i -f`

- Stampa la dimensione di ogni file e la dimensione totale di ogni cartella, in formato leggibile dall'utente:

`tree -s -h --du`

- Stampa i file all'interno dell'albero gerarchico, utilizzando espressioni di metacaratteri (glob pattern) per escludere le cartelle che non contengono file corrispondenti alla ricerca:

`tree -P '{{*.txt}}' --prune`

- Stampa le cartelle all'interno dell'albero gerarchico, utilizzando espressioni di metacaratteri (glob pattern) per escludere le cartelle che non sono progenitori di quelle desiderate:

`tree -P {{nomi_di_cartelle}} --matchdirs --prune`

- Stampa l'albero ignorando le cartelle date:

`tree -I '{{nome_cartella1|nome_cartella2}}'`
