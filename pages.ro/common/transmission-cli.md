# transmission-cli

> Un client BitTorrent cu linie de comandă uşoară.
> Acest instrument a fost învechit, vă rugăm să consultați „transmisie-telecomandă”.
> Mai multe informaţii: <https://transmissionbt.com>

- Descarcă un torent specific:

`transmission-cli {{url|magnet|path/to/file}}`

- Descărcați un torent într-un anumit director:

`transmission-cli --download-dir {{path/to/download_directory}} {{url|magnet|path/to/file}}`

- Creați un fișier torrent dintr-un anumit fișier sau director:

`transmission-cli --new {{path/to/source_file_or_directory}}`

- Setați limita de viteză de descărcare la 50 KB/s:

`transmission-cli --downlimit {{50}} {{url|magnet|path/to/file}}`

- Setați limita de viteză de încărcare la 50 KB/s:

`transmission-cli --uplimit {{50}} {{url|magnet|path/to/file}}`

- Utilizați un anumit port pentru conexiuni:

`transmission-cli --port {{port_number}} {{url|magnet|path/to/file}}`

- Criptare forțată pentru conexiuni peer:

`transmission-cli --encryption-required {{url|magnet|path/to/file}}`

- Utilizați un blocklist peer formatat în BlueTack-:

`transmission-cli --blocklist {{blocklist_url|path/to/blocklist}} {{url|magnet|path/to/file}}`
