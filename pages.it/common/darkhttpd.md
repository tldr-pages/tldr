# darkhttpd

> Web server Darkhttpd.
> Maggiori informazioni: <https://unix4lyfe.org/darkhttpd>.

- Avvia il server utilizzando la directory specificata come document root:

`darkhttpd {{percorso/della/docroot}}`

- Avvia il server su una specifica porta (8080 di default per utenti non root):

`darkhttpd {{percorso/della/docroot}} --port {{porta}}`

- Ascolta solo su uno specifico indirizzo IP (di default, il server ascolta su tutte le interfacce):

`darkhttpd {{percorso/della/docroot}} --addr {{indirizzo_ip}}`
