# transmission-create

> Maak BitTorrent `.torrent` bestanden.
> Bekijk ook: `transmission`.
> Meer informatie: <https://manned.org/transmission-create>.

- Maak een torrent met een stukgrootte van 2048 KB:

`transmission-create -o {{pad/naar/voorbeeld.torrent}} --tracker {{aankondigings-url_van_tracker}} --piecesize {{2048}} {{pad/naar/bestand_of_map}}`

- Maak een privé torrent met een stukgrootte van 2048 KB:

`transmission-create -p -o {{pad/naar/voorbeeld.torrent}} --tracker {{aankondigings-url_van_tracker}} --piecesize {{2048}} {{pad/naar/bestand_of_map}}`

- Maak een torrent met een opmerking:

`transmission-create -o {{pad/naar/voorbeeld.torrent}} --tracker {{tracker_url1}} -c {{opmerking}} {{pad/naar/bestand_of_map}}`

- Maak een torrent met meerdere trackers:

`transmission-create -o {{pad/naar/voorbeeld.torrent}} --tracker {{tracker_url1}} --tracker {{tracker_url2}} {{pad/naar/bestand_of_map}}`

- Toon de help-pagina:

`transmission-create --help`
