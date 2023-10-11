# ag

> The Silver Searcher. Come `ack`, ma più veloce.
> Maggiori informazioni: <https://github.com/ggreer/the_silver_searcher>.

- Trova file contenenti "foo" e mostra le corrisponenti linee contenenti il termine:

`ag {{foo}}`

- Trova file contenenti "foo" in una specifica directory:

`ag {{foo}} {{percorso/della/directory}}`

- Trova file contenenti "foo" elencandone solamente i nomi:

`ag -l {{foo}}`

- Trova file contenenti "FOO" senza distinguere tra maiuscole e minuscole, e stampa solo il termine trovato piuttosto che l'intera linea:

`ag -i -o {{FOO}}`

- Trova "foo" in file il quale nome contiene "bar":

`ag {{foo}} -G {{bar}}`

- Trova file il quale contenuto soddisfi una determinata espressione regolare:

`ag '{{espressione_regolare}}'`

- Trova file il quale nome contiene "foo":

`ag -g {{foo}}`
