# transmission-create

> Maak BitTorrent `.torrent` bestanden.
> Zie ook: `transmission`.
> Meer informatie: <https://manned.org/transmission-create>.

- Maak een torrent met een specifieke stukgrootte (in KB):

`transmission-create {{[-o|--outfile]}} {{pad/naar/voorbeeld.torrent}} {{[-t|--tracker]}} {{aankondigings-url_van_tracker}} {{[-s|--piecesize]}} {{2048}} {{pad/naar/bestand_of_map}}`

- Maak een privé torrent met een specifieke stukgrootte (in KB):

`transmission-create {{[-p|--private]}} {{[-o|--outfile]}} {{pad/naar/voorbeeld.torrent}} {{[-t|--tracker]}} {{aankondigings-url_van_tracker}} {{[-s|--piecesize]}} {{2048}} {{pad/naar/bestand_of_map}}`

- Maak een torrent met een opmerking:

`transmission-create {{[-o|--outfile]}} {{pad/naar/voorbeeld.torrent}} {{[-t|--tracker]}} {{tracker_url1}} {{[-c|--comment]}} {{opmerking}} {{pad/naar/bestand_of_map}}`

- Maak een torrent met meerdere trackers:

`transmission-create {{[-o|--outfile]}} {{pad/naar/voorbeeld.torrent}} {{[-t|--tracker]}} {{tracker_url1}} {{[-t|--tracker]}} {{tracker_url2}} {{pad/naar/bestand_of_map}}`

- Toon de help-pagina:

`transmission-create {{[-h|--help]}}`
