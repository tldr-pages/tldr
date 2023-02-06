# pdfseparate

> Portable Document Format (PDF) fájl oldalkivonatoló. További információ: <https://manpages.debian.org/unstable/poppler-utils/pdfseparate.1.en.html>.

- Oldalak kivonása a PDF-fájlból, és külön PDF-fájlt készít minden egyes oldalhoz:

`pdfseparate {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- Adja meg az első/kezdő oldalt a kivonáshoz:

`pdfseparate -f {{3}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- Az utolsó oldal megadása a kivonáshoz:

`pdfseparate -l {{10}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`
