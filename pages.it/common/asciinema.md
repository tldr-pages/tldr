# asciinema

> Registra e riproduci sessioni di terminale, condividendole opzionalmente su asciiname.org.
> Maggiori informazioni: <https://docs.asciinema.org/manual/cli/usage>.

- Associa l'installazione locale di `asciiname` ad un account di asciiname.org:

`asciinema auth`

- Avvia una nuova registrazione (una volta terminata, verrà chiesto se caricarla o salvarla localmente):

`asciinema rec`

- Avvia una nuova registrazione e salvala come file locale:

`asciinema rec {{percorso/del/registrazione.cast}}`

- Riproduci una sessione da un file locale:

`asciinema play {{percorso/del/registrazione.cast}}`

- Riproducei una sessione da asciinema.org:

`asciinema play https://asciinema.org/a/{{id_registrazione}}`

- Avvia una nuova registrazione, limitando qualsiasi periodo di [i]nattività a 2.5 secondi:

`asciinema rec -i 2.5`

- Stampa l'output completo di una sessione locale:

`asciinema cat {{percorso/del/registrazione.cast}}`

- Carica una sessione locale su asciinama.org:

`asciinema upload {{percorso/del/registrazione.cast}}`
