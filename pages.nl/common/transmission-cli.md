# transmission-cli

> Een lichtgewicht, command-line BitTorrent client.
> Deze tool is verouderd, bekijk `transmission-remote`.
> Meer informatie: <https://transmissionbt.com>.

- Download een specifieke torrent:

`transmission-cli {{url|magnet|pad/naar/bestand}}`

- Download een torrent naar een specifieke map:

`transmission-cli --download-dir {{pad/naar/download_map}} {{url|magnet|pad/naar/bestand}}`

- Maak een torrent bestand van een specifiek bestand of map:

`transmission-cli --new {{pad/naar/source_bestand_of_map}}`

- Zet de download snelheid limiet naar 50 KB/s:

`transmission-cli --downlimit {{50}} {{url|magnet|pad/naar/bestand}}`

- Zet de upload snelheid limiet naar 50 KB/s:

`transmission-cli --uplimit {{50}} {{url|magnet|pad/naar/bestand}}`

- Gebruik een specifieke poort voor verbindingen:

`transmission-cli --port {{port_number}} {{url|magnet|pad/naar/bestand}}`

- Forceer versleuteling voor alle peer-verbindingen:

`transmission-cli --encryption-required {{url|magnet|pad/naar/bestand}}`

- Gebruik een Bluetack-geformatteerde peer blocklist:

`transmission-cli --blocklist {{blocklist_url|pad/naar/blocklist}} {{url|magnet|pad/naar/bestand}}`
