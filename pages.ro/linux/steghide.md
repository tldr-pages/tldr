# steghide

> Instrument Steganography pentru formatele de fișiere JPEG, BMP, WAV și AU.
> Mai multe informaţii: <https://github.com/StefanoDeVuono/steghide>

- Încorporarea datelor într-o imagine PNG, care solicită o frază de acces:

`steghide embed --coverfile {{path/to/image.png}} --embedfile {{path/to/data.txt}}`

- Extragerea datelor dintr-un fișier audio WAV:

`steghide extract --stegofile {{path/to/sound.wav}}`

- Afișează informații despre fișier, încercând să detecteze un fișier încorporat:

`steghide info {{path/to/file.jpg}}`

- Încorporarea datelor într-o imagine JPEG, utilizând compresia maximă:

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --compress {{9}}`

- Obțineți lista algoritmilor și modurilor de criptare acceptate:

`steghide encinfo`

- Încorporarea datelor criptate într-o imagine JPEG, de exemplu cu Blowfish în modul CBC:

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --encryption {{blowfish|...}} {{cbc|...}}`
