# alien

> Különböző telepítőcsomagok átalakítása más formátumokra. További információ: <https://manned.org/alien>.

- Konvertáljon egy adott telepítőfájlt Debian formátumba (`.deb` kiterjesztés):

`sudo alien --to-deb {{path/to/file}}`

- Egy adott telepítési fájl átalakítása Red Hat formátumba (`.rpm` kiterjesztés):

`sudo alien --to-rpm {{path/to/file}}`

- Egy adott telepítőfájl átalakítása Slackware telepítőfájlba (`.tgz` kiterjesztés):

`sudo alien --to-tgz {{path/to/file}}`

- Konvertáljon egy adott telepítőfájlt Debian formátumba és telepítse a rendszerre:

`sudo alien --to-deb --install {{path/to/file}}`
