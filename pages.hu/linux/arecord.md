# arecord

> Hangrögzítő az ALSA hangkártya-illesztőprogramhoz. További információ: <https://manned.org/arecord>.

- Vegyen fel egy részletet "CD" minőségben (befejezés után Ctrl-C-vel fejezze be):

`arecord -vv --format=cd {{path/to/file.wav}}`

- Egy részlet felvétele "CD" minőségben, 10 másodperces fix időtartamban:

`arecord -vv --format=cd --duration={{10}} {{path/to/file.wav}}`

- Egy részlet felvétele és mentése MP3-ként (befejezés után Ctrl-C-vel befejezni):

`arecord -vv --format=cd --file-type raw | lame -r - {{path/to/file.mp3}}`

- Az összes hangkártya és digitális audioeszköz felsorolása:

`arecord --list-devices`

- Interaktív felület engedélyezése (pl. a lejátszáshoz vagy szüneteltetéshez a szóköz vagy az enter billentyű használata):

`arecord --interactive`
