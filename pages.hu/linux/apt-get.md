# apt-get

> Debian és Ubuntu csomagkezelő segédprogram. Csomagok keresése a `apt-cache` segítségével. További információ: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Frissítse az elérhető csomagok és verziók listáját (ajánlott ezt a többi `apt-get` parancs előtt futtatni):

`apt-get update`

- Telepítsen egy csomagot, vagy frissítse azt a legújabb elérhető verzióra:

`apt-get install {{package}}`

- Egy csomag eltávolítása:

`apt-get remove {{package}}`

- Egy csomag és konfigurációs fájljai eltávolítása:

`apt-get purge {{package}}`

- Az összes telepített csomag frissítése a legújabb elérhető verzióra:

`apt-get upgrade`

- A helyi tároló megtisztítása - a megszakított letöltésekből származó, már nem letölthető csomagfájlok (`.deb`) eltávolítása:

`apt-get autoclean`

- A már nem szükséges csomagok eltávolítása:

`apt-get autoremove`

- A telepített csomagok frissítése (mint a `upgrade`), de az elavult csomagok eltávolítása és további csomagok telepítése az új függőségek kielégítésére:

`apt-get dist-upgrade`
