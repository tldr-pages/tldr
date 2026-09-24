# aria2c

> Utilità di download veloce multiprotocollo.
> Supporta HTTP(S), FTP, SFTP, BitTorrent e Metalink.
> Vedi anche: `axel`.
> Maggiori informazioni: <https://aria2.github.io/manual/en/html/aria2c.html>.

- Scarica un URI specifico in un file:

`aria2c "{{url}}"`

- Scarica un file da un URI con nome di output specifico:

`aria2c {{[-o|--out]}} {{percorso/al/file}} "{{url}}"`

- Scarica più file diversi in parallelo:

`aria2c {{[-Z|--force-sequential=true]}} {{"url1" "url2" ...}}`

- Scarica lo stesso file da diversi mirror verificando il checksum:

`aria2c --checksum {{sha-256}}={{hash}} {{"url1" "url2" ...}}`

- Scarica gli URI elencati in un file con numero specifico di download paralleli:

`aria2c {{[-i|--input-file]}} {{percorso/al/file}} {{[-j|--max-concurrent-downloads]}} {{numero_download}}`

- Scarica con più connessioni:

`aria2c {{[-s|--split]}} {{numero_connessioni}} "{{url}}"`

- Download FTP con username e password:

`aria2c --ftp-user {{username}} --ftp-passwd {{password}} "{{url}}"`

- Limita la velocità di download in byte/s:

`aria2c --max-download-limit {{velocità}} "{{url}}"`
