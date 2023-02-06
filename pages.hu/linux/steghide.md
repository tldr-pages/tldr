# steghide

> Steganográfiai eszköz JPEG, BMP, WAV és AU fájlformátumokhoz. További információ: <https://github.com/StefanoDeVuono/steghide>.

- Adatok beágyazása egy PNG-be, jelszó megadására kérve:

`steghide embed --coverfile {{path/to/image.png}} --embedfile {{path/to/data.txt}}`

- Adatok kivonása egy WAV hangfájlból:

`steghide extract --stegofile {{path/to/sound.wav}}`

- Fájlinformációk megjelenítése, a beágyazott fájl felismerésére tett kísérlet:

`steghide info {{path/to/file.jpg}}`

- Adatok beágyazása JPEG képbe, maximális tömörítéssel:

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --compress {{9}}`

- A támogatott titkosítási algoritmusok és módok listájának lekérdezése:

`steghide encinfo`

- Titkosított adatok beágyazása JPEG-képbe, pl. Blowfish-sel CBC módban:

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --encryption {{blowfish|...}} {{cbc|...}}`
