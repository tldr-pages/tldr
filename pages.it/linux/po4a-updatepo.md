# po4a-updatepo

> Aggiorna la traduzione (in formato PO) di una documentazione.
> Maggiori informazioni: <https://www.po4a.org/man/man1/po4a-updatepo.1.php>.

- Aggiorna un file PO in base alla modifica del suo file originale:

`po4a-updatepo --format {{testo}} --master {{percorso/master.txt}} --po {{percorso/risultato.po}}`

- Elenca i formati disponibili:

`po4a-updatepo --help-format`

- Aggiorna diversi file PO in base alla modifica del loro file originale:

`po4a-updatepo --format {{testo}} --master {{percorso/master.txt}} --po {{percorso/po1.po}} --po {{percorso/po2.po}}`
