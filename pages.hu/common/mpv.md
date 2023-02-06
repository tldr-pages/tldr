# mpv

> MPlayer alapú audio/video lejátszó. További információ [: https://mpv.io](https://mpv.io).

- Videó- vagy hangfájl lejátszása:

`mpv {{path/to/file}}`

- Videó- vagy hangfájl lejátszása egy URL-címről:

`mpv '{{https://www.youtube.com/watch?v=dQw4w9WgXcQ}}'`

- Ugrás előre/vissza 5 másodpercet:

`LEFT <or> RIGHT`

- Ugrás előre/vissza 1 percig:

`DOWN <or> UP`

- A lejátszási sebesség csökkentése vagy növelése 10%-kal:

`[ <or> ]`

- A fájl lejátszása megadott sebességgel (0,01 és 100 között, alapértelmezett 1):

`mpv --speed {{speed}} {{path/to/file}}`

- Fájl lejátszása a `mpv.conf` fájlban meghatározott profillal:

`mpv --profile {{profile_name}} {{path/to/file}}`

- A webkamera vagy más videó bemeneti eszköz kimenetének megjelenítése:

`mpv /dev/{{video0}}`
