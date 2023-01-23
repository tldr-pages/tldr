# nkf

> Hálózati kanji szűrő. Átalakítja a kanji kódot egyik kódolásból a másikba. További információ: <https://manned.org/nkf>.

- Átalakítás UTF-8 kódolásra:

`nkf -w {{path/to/file.txt}}`

- Átalakítás SHIFT_JIS kódolásra:

`nkf -s {{path/to/file.txt}}`

- Konvertálás UTF-8 kódolásra és a fájl felülírása:

`nkf -w --overwrite {{path/to/file.txt}}`

- Új sor kódjának LF-re állítása és felülírása (UNIX típus):

`nkf -d --overwrite {{path/to/file.txt}}`

- Új sor kódját CRLF-re állítsa és felülírja (windows típus):

`nkf -c --overwrite {{path/to/file.txt}}`

- Mime fájl visszafejtése és felülírása:

`nkf -m --overwrite {{path/to/file.txt}}`
