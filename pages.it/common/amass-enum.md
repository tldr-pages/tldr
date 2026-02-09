# amass enum

> Trova i sottodomini di un dominio.
> Maggiori informazioni: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Trova (passivamente) i sottodomini di un [d]ominio:

`amass enum -d {{nome_dom}}`

- Trova i sottodomini di un [d]ominio e li verifica attivamente tentando di risolvere i sottodomini trovati:

`amass enum -active -d {{nome_dom}} -p {{80,443,8080}}`

- Esegue una ricerca a forza bruta per i sottodomini:

`amass enum -brute -d {{nome_dom}}`

- Salva i risultati in un file di testo:

`amass enum -o {{file_output}} -d {{nome_dom}}`

- Salva l’output del terminale in un file e altri output dettagliati in una directory:

`amass enum -o {{file_output}} -dir {{percorso/della/directory}} -d {{nome_dom}}`

- Elenca tutte le fonti dati disponibili:

`amass enum -list`
