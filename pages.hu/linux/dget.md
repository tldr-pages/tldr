# dget

> Debian csomagok letöltése. További információ: <https://manpages.debian.org/dget>.

- Bináris csomag letöltése:

`dget {{package_name}}`

- Töltsön le és vonja ki a csomag forrását a `.dsc` fájlból:

`dget {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

- Töltsön le egy csomag forrását tartalmazó tarballt a `.dsc` fájlból, de ne bontsa ki:

`dget -d {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`
