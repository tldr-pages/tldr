# pngcrush

> Utilitar de compresie a imaginii PNG.
> Mai multe informaţii: <https://pmt.sourceforge.io/pngcrush>

- Comprimați un fișier PNG:

`pngcrush {{in.png}} {{out.png}}`

- Comprimați toate PNG-urile și ieșiți în director:

`pngcrush -d {{path/to/output}} *.png`

- Comprimați fișierul PNG cu toți 114 algoritmi disponibili și alegeți cel mai bun rezultat:

`pngcrush -rem allb -brute -reduce {{in.png}} {{out.png}}`
