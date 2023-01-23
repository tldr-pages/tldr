# iconv

> Szöveget konvertál egyik kódolásból egy másikba. További információ: <https://manned.org/iconv>.

- Fájl átalakítása egy adott kódolásra, és nyomtatás a `stdout` címre:

`iconv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- Fájl átalakítása az aktuális nyelvterület kódolásához, és kimenet egy fájlba:

`iconv -f {{from_encoding}} {{input_file}} > {{output_file}}`

- Támogatott kódolások listája:

`iconv -l`
