# mkvmerge

> Multimédia folyamokat egyesít és kivonatol. További információ: <https://mkvtoolnix.download/doc/mkvmerge.html>.

- Információk megjelenítése egy Matroska-fájlról:

`mkvmerge --identify {{path/to/file.mkv}}`

- Egy adott fájl 1. sávjának hanganyagának kivonása:

`mkvextract tracks {{path/to/file.mkv}} {{1}}:{{path/to/output.webm}}`

- A felirat kivonása egy adott fájl 3. sávjából:

`mkvextract tracks {{path/to/file.mkv}} {{3}}:{{path/to/subs.srt}}`

- Felirat-sáv hozzáadása egy fájlhoz:

`mkvmerge --output {{path/to/output.mkv}} {{path/to/file.mkv}} {{path/to/subs.srt}}`
