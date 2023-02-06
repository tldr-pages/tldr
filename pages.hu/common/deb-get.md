# deb-get

> `apt-get` funkcionalitás a `.deb` csomagok számára, amelyeket harmadik fél tárolókban vagy közvetlen letöltés útján tettek közzé. Működik olyan Linux disztribúciókkal, amelyek a `apt-get`-t használják. További információ: <https://github.com/wimpysworld/deb-get>.

- Az elérhető csomagok és verziók listájának frissítése:

`sudo deb-get update`

- Egy adott csomag keresése:

`sudo deb-get search {{package}}`

- Információk megjelenítése egy csomagról:

`sudo deb-get show {{package}}`

- Telepítsen egy csomagot, vagy frissítse azt a legújabb elérhető verzióra:

`sudo deb-get install {{package}}`

- Egy csomag eltávolítása (a `purge` használata helyette a csomag konfigurációs fájljait is eltávolítja):

`sudo deb-get remove {{package}}`

- Az összes telepített csomag frissítése a legújabb elérhető verzióra:

`sudo deb-get upgrade`

- Az összes elérhető csomag listázása:

`deb-get list`
