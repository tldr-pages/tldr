# exiv2

> Instrument de manipulare a metadatelor imaginii.
> Mai multe informaţii: <https://www.exiv2.org/manpage.html>

- Imprimați un rezumat al imaginii metadate Exif:

`exiv2 {{path/to/file}}`

- Imprimați toate metadatele (Exif, IPTC, XMP) cu valori interpretate:

`exiv2 -P kt {{path/to/file}}`

- Imprimați toate metadatele cu valori brute:

`exiv2 -P kv {{path/to/file}}`

- Ștergeți toate metadatele dintr-o imagine:

`exiv2 -d a {{path/to/file}}`

- Ștergeți toate metadatele, păstrând timestamp fișier:

`exiv2 -d a -k {{path/to/file}}`

- Redenumiți fișierul, preașteptând data și ora din metadate (nu din marcajul de timp al fișierului):

`exiv2 -r {{'%Y%m%d_%H%M%S_:basename:'}} {{path/to/file}}`
