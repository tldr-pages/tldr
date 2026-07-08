# gnome-screenshot

> Cattura lo schermo, una finestra o un'area definita dall'utente e salva l'immagine in un file.
> Maggiori informazioni: <https://manned.org/gnome-screenshot>.

- Cattura uno screenshot e lo salva nella posizione predefinita, normalmente `~/Pictures`:

`gnome-screenshot`

- Cattura uno screenshot e lo salva nel percorso file indicato:

`gnome-screenshot {{[-f|--file]}} {{path/to/file}}`

- Cattura uno screenshot e lo salva negli appunti:

`gnome-screenshot {{[-c|--clipboard]}}`

- Cattura uno screenshot dopo il numero di secondi specificato:

`gnome-screenshot {{[-d|--delay]}} {{5}}`

- Avvia l'interfaccia grafica GNOME Screenshot:

`gnome-screenshot {{[-i|--interactive]}}`

- Cattura uno screenshot della finestra corrente e lo salva nel percorso file specificato:

`gnome-screenshot {{[-w|--window]}} {{[-f|--file]}} {{path/to/file}}`

- Cattura uno screenshot dopo il numero di secondi specificato e lo salva negli appunti:

`gnome-screenshot {{[-d|--delay]}} {{10}} {{[-c|--clipboard]}}`

- Mostra versione:

`gnome-screenshot --version`
