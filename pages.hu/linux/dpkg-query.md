# dpkg-query

> A telepített csomagokról szóló információkat megjelenítő eszköz. További információ: <https://manpages.debian.org/latest/dpkg/dpkg-query.1.html>.

- Az összes telepített csomag listázása:

`dpkg-query --list`

- Egy mintának megfelelő telepített csomagok listázása:

`dpkg-query --list '{{libc6*}}'`

- Egy csomag által telepített összes fájl listázása:

`dpkg-query --listfiles {{libc6}}`

- Információk megjelenítése egy csomagról:

`dpkg-query --status {{libc6}}`

- Olyan csomagok keresése, amelyek egy adott mintának megfelelő fájlokat tartalmaznak:

`dpkg-query --search {{/etc/ld.so.conf.d}}`
