# debtap

> Debian csomagok Arch Linux csomagokká konvertálása. Lásd még: `pacman-upgrade`. További információ: <https://github.com/helixarch/debtap>.

- A debtap adatbázis frissítése (az első futtatás előtt):

`sudo debtap --update`

- A megadott csomag átalakítása:

`debtap {{path/to/package.deb}}`

- A megadott csomag átalakítása minden kérdés megkerülésével, kivéve a metaadatfájlok szerkesztését:

`debtap --quiet {{path/to/package.deb}}`

- PKGBUILD fájl generálása:

`debtap --pkgbuild {{path/to/package.deb}}`
