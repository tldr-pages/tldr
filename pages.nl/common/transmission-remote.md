# transmission-remote

> Externe besturingshulpprogramma voor `transmission-daemon` en `transmission`.
> Meer informatie: <https://transmissionbt.com>.

- Voeg een torrentbestand of magnet-link toe aan Transmission en download naar een opgegeven map:

`transmission-remote {{hostname}} -a {{torrent|url}} -w {{/pad/naar/download_map}}`

- Verander de standaard downloadmap:

`transmission-remote {{hostname}} -w {{/pad/naar/download_map}}`

- Toon alle torrents:

`transmission-remote {{hostname}} --list`

- Start torrent 1 en 2, stop torrent 3:

`transmission-remote {{hostname}} -t "{{1,2}}" --start -t {{3}} --stop`

- Verwijder torrent 1 en 2 en verwijder ook alle lokale gegevens voor torrent 2:

`transmission-remote {{hostname}} -t {{1}} --remove -t {{2}} --remove-and-delete`

- Stop alle torrents:

`transmission-remote {{hostname}} -t {{all}} --stop`

- Verplaats torrents 1-10 en 15-20 naar een nieuwe map (die wordt aangemaakt als deze nog niet bestaat):

`transmission-remote {{hostname}} -t "{{1-10,15-20}}" --move {{/pad/naar/nieuwe_map}}`
