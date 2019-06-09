# aria2

> Strumento di download da linea di comando leggero, multi-protocollo e multi-sorgente.
> Supporta HTTP, HTTPS, FTP, SFTP, BitTorrent e Metalink.
> Maggiori informazioni: <https://aria2.github.io/>.

- Scarica una risorsa web:

`aria2c {{http://example.org/myLinux.iso}}`

- Scarica una risorsa da sorgenti multiple:

`aria2c {{http://mirror1.org/myLinux.iso}} {{http://mirror2.org/myLinux.iso}}`

- Scarica utilizzando 2 connessioni per host:

`aria2c -x{{2}} {{http://example.org/myLinux.iso}}`

- Scarica un file da un URI Metalink:

`aria2c {{http://example.org/myLinux.metalink}}`

- Scarica da un URI BitTorrent:

`aria2c {{http://example.org/myLinux.torrent}}`

- Scarica da un Magnet URI BitTorrent:

`aria2c {{'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'}}`

- Scarica dagli URI listati in un file:

`aria2c -i {{uris.txt}}`
