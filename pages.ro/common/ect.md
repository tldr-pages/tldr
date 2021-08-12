# ect

> Instrument de compresie eficient.
> Optimizator de fișiere scris în C++. Acesta acceptă fișiere `.png`, `.jpg`, `.gzip `și `.zip`.
> Mai multe informaţii: <https://github.com/fhanau/Efficient-Compression-Tool>

- Comprimare fișier:

`ect {{path/to/file.png}}`

- Comprimați un fișier cu nivelul de compresie specificat și multithreading (1 = Cel mai rapid (cel mai rău), 9 = Cel mai lent (cel mai bun), implicit este 3):

`ect -{{9}} --mt-deflate {{path/to/file.zip}}`

- Comprimați toate fișierele într-un director recursiv:

`ect -recurse {{path/to/directory}}`

- Comprimați un fișier, păstrând timpul original de modificare:

`ect -keep {{path/to/file.png}}`

- Comprimare fișier, dezmembrare metadate:

`ect -strip {{path/to/file.png}}`
