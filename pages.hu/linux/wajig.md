# wajig

> Egyszerűsített, mindenre kiterjedő rendszersegítő eszköz Debian-alapú rendszerekhez. További információ: <https://wajig.togaware.com>.

- Az elérhető csomagok és verziók listájának frissítése:

`wajig update`

- Telepítsen egy csomagot, vagy frissítse azt a legújabb elérhető verzióra:

`wajig install {{package}}`

- Egy csomag és a hozzá tartozó konfigurációs fájlok eltávolítása:

`wajig purge {{package}}`

- Frissítés, majd dist-upgrade végrehajtása:

`wajig daily-upgrade`

- A telepített csomagok méretének megjelenítése:

`wajig sizes`

- Az összes telepített csomag verziójának és terjesztésének listázása:

`wajig versions`

- A frissíthető csomagok verzióinak listázása:

`wajig toupgrade`

- Azoknak a csomagoknak a megjelenítése, amelyek valamilyen formában függnek az adott csomagtól:

`wajig dependents {{package}}`
