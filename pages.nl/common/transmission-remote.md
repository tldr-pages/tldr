# transmission-remote

> Externe besturingshulpprogramma voor `transmission-daemon` en `transmission`.
> Meer informatie: <https://manned.org/transmission-remote>.

- Voeg een torrentbestand of magnet-link toe aan Transmission en download naar een opgegeven map:

`transmission-remote {{hostnaam}} {{[-a|--all]}} {{torrent|url}} {{[-w|--download-dir]}} /{{pad/naar/download_map}}`

- Verander de standaard downloadmap:

`transmission-remote {{hostnaam}} {{[-w|--download-dir]}} /{{pad/naar/download_map}}`

- Toon alle torrents:

`transmission-remote {{hostnaam}} {{[-l|--list]}}`

- Start torrent 1 en 2, stop torrent 3:

`transmission-remote {{hostnaam}} {{[-t|--torrent]}} "1,2" {{[-s|--start]}} {{[-t|--torrent]}} 3 {{[-S|--stop]}}`

- Verwijder torrent 1 en 2 en verwijder ook alle lokale gegevens voor torrent 2:

`transmission-remote {{hostnaam}} {{[-t|--torrent]}} 1 {{[-r|--remove]}} {{[-t|--torrent]}} 2 {{[-rad|--remove-and-delete]}}`

- Stop alle torrents:

`transmission-remote {{hostnaam}} {{[-t|--torrent]}} {{all}} {{[-S|--stop]}}`

- Verplaats torrents 1-10 en 15-20 naar een nieuwe map (die wordt aangemaakt als deze nog niet bestaat):

`transmission-remote {{hostnaam}} {{[-t|--torrent]}} "1-10,15-20" --move /{{pad/naar/nieuwe_map}}`
