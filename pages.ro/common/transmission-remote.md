# transmission-remote

> Utilitar de control de la distanță pentru transmisie-daemon și transmisie.
> Mai multe informaţii: <https://transmissionbt.com>

- Adăugați un fișier torrent sau un link magnet la Transmisie și descărcați într-un director specificat:

`transmission-remote {{hostname}} -a {{torrent|url}} -w {{/path/to/download_directory}}`

- Modificați directorul de descărcare implicit:

`transmission-remote {{hostname}} -w {{/path/to/download_directory}}`

- Listează toate torentele:

`transmission-remote {{hostname}} --list`

- Porniți torrent 1 și 2, opriți torrent 3:

`transmission-remote {{hostname}} -t "{{1,2}}" --start -t {{3}} --stop`

- Eliminați torrent 1 și 2 și, de asemenea, ștergeți datele locale pentru torrent 2:

`transmission-remote {{hostname}} -t {{1}} --remove -t {{2}} --remove-and-delete`

- Opriţi toate torentele:

`transmission-remote {{hostname}} -t {{all}} --stop`

- Mutați torentele 1-10 și 15-20 într-un nou director (care va fi creat dacă nu există):

`transmission-remote {{hostname}} -t "{{1-10,15-20}}" --move {{/path/to/new_directory}}`
