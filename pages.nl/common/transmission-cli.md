# transmission-cli

> Een lichtgewicht, command-line BitTorrent client.
> Deze tool is verouderd, bekijk `transmission-remote`.
> Meer informatie: <https://manned.org/transmission-cli>.

- Download een specifieke torrent:

`transmission-cli {{url|magnet|pad/naar/bestand}}`

- Download een torrent naar een specifieke map:

`transmission-cli {{[-w|--download-dir]}} {{pad/naar/download_map}} {{url|magnet|pad/naar/bestand}}`

- Maak een torrent bestand van een specifiek bestand of map:

`transmission-cli --new {{pad/naar/bronbestand_of_map}}`

- Zet de download snelheid limiet naar 50 KB/s:

`transmission-cli {{[-d|--downlimit]}} {{50}} {{url|magnet|pad/naar/bestand}}`

- Zet de upload snelheid limiet naar 50 KB/s:

`transmission-cli {{[-u|--uplimit]}} {{50}} {{url|magnet|pad/naar/bestand}}`

- Gebruik een specifieke poort voor verbindingen:

`transmission-cli {{[-p|--port]}} {{poort_nummer}} {{url|magnet|pad/naar/bestand}}`

- Forceer versleuteling voor alle peer-verbindingen:

`transmission-cli {{[-er|--encryption-required]}} {{url|magnet|pad/naar/bestand}}`

- Gebruik een Bluetack-geformatteerde peer blocklist:

`transmission-cli {{[-b|--blocklist]}} {{blocklist_url|pad/naar/blocklist}} {{url|magnet|pad/naar/bestand}}`
