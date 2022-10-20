# deluge

> Client BItTorrent da linea di comando.
> Maggiori informazioni: <https://deluge-torrent.org>.

- Scarica un torrent:

`deluge {{url|magnet|percorso/del/file}}`

- Scarica un torrent utilizzando uno specifico file di configurazione:

`deluge -c {{percorso/del/file_configurazione}} {{url|magnet|percorso/del/file}}`

- Scarica un torrent ed avvia una specifica interfaccia utente:

`deluge -u {{gtk|web|console}} {{url|magnet|percorso/del/file}}`

- Scarica un torrent e scrivi il log in un file:

`deluge -l {{percorso/del/file_log}} {{url|magnet|percorso/del/file}}`
