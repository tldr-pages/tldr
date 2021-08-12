# nkf

> Filtru kanji rețea.
> Convertește codul kanji dintr-o codificare în alta.

- Conversia la codificarea UTF-8:

`nkf -w {{path/to/file.txt}}`

- Conversia la codificarea SHIFT_JIS:

`nkf -s {{path/to/file.txt}}`

- Conversia la codificarea UTF-8 și suprascrie fișierul:

`nkf -w --overwrite {{path/to/file.txt}}`

- Setați noul cod de linie la LF și suprascrieți (tip unix):

`nkf -d --overwrite {{path/to/file.txt}}`

- Setați codul de linie nou la CRLF și suprascrieți (tipul de ferestre):

`nkf -c --overwrite {{path/to/file.txt}}`

- Decriptează fișierul mime și suprascrie:

`nkf -m --overwrite {{path/to/file.txt}}`
