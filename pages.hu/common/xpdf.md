# xpdf

> Portable Document Format (PDF) fájlnéző. További információ: <https://www.xpdfreader.com/xpdf-man.html>.

- PDF-fájl megnyitása:

`xpdf {{path/to/file.pdf}}`

- Egy adott oldal megnyitása egy PDF-fájlban:

`xpdf {{path/to/file.pdf}} :{{page_number}}`

- Tömörített PDF-fájl megnyitása:

`xpdf {{path/to/file.pdf.tar}}`

- PDF-fájl megnyitása teljes képernyős módban:

`xpdf -fullscreen {{path/to/file.pdf}}`

- A kezdeti nagyítás megadása:

`xpdf -z {{75}}% {{path/to/file.pdf}}`

- A kezdeti nagyítás megadása oldalszélességben vagy teljes oldalon:

`xpdf -z {{page|width}} {{path/to/file.pdf}}`
