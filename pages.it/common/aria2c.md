# aria2c

> Veloce utilità di download.
> Supporta HTTP(S), FTP, SFTP, BitTorrent, e Metalink.
> Maggiori informazioni: <https://aria2.github.io>.

- Scarica un file da un URI:

`aria2c {{url}}`

- Scarica più file da diverse sorgenti:

`aria2c {{url_1}} {{url_2}}`

- Scarica gli URI elencati in un file:

`aria2c -i {{filename}}`

- Esegui il download con connessioni multiple:

`aria2c -s {{numero_connessioni}} {{url}}`

- Scarica via FTP con username e password:

`aria2c --ftp-user={{username}} --ftp-passwd={{password}} {{url}}`

- Limita la velocità di download (in byte al secondo):

`aria2c --max-download-limit={{velocità}} {{url}}`
