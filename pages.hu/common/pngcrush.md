# pngcrush

> PNG tömörítő segédprogram. További információ: <https://pmt.sourceforge.io/pngcrush>.

- PNG fájl tömörítése:

`pngcrush {{in.png}} {{out.png}}`

- Az összes PNG fájl tömörítése és kimenete a megadott könyvtárba:

`pngcrush -d {{path/to/output}} *.png`

- A PNG-fájl tömörítése mind a 114 elérhető algoritmussal és a legjobb eredmény kiválasztása:

`pngcrush -rem allb -brute -reduce {{in.png}} {{out.png}}`
