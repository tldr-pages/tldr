# deemix

> A Deezloader Remix hamvaiból épített barebone deezer letöltő könyvtár. Használható önálló CLI alkalmazásként, vagy az API segítségével egy felhasználói felületbe implementálva. További információ [: https://deemix.app](https://deemix.app).

- Sáv vagy lejátszási lista letöltése:

`deemix {{https://www.deezer.com/us/track/00000000}}`

- Sáv / lejátszási lista letöltése egy adott bitrátával:

`deemix --bitrate {{FLAC|MP3}} {{url}}`

- Letöltés egy adott elérési útvonalra:

`deemix --bitrate {{bitrate}} --path {{path}} {{url}}`

- Hordozható deemix config létrehozása az aktuális könyvtárban:

`deemix --portable --bitrate {{bitrate}} --path {{path}} {{url}}`
