# pacman --query

> Arch Linux csomagkezelő segédprogram. További információ: <https://man.archlinux.org/man/pacman.8>.

- Telepített csomagok és verziók listája:

`pacman --query`

- Csak a kifejezetten telepített csomagok és verziók listázása:

`pacman --query --explicit`

- Keresse meg, melyik csomag tulajdonában van egy fájl:

`pacman --query --owns {{filename}}`

- Információk megjelenítése egy telepített csomagról:

`pacman --query --info {{package_name}}`

- Egy csomag által birtokolt fájlok listázása:

`pacman --query --list {{package_name}}`

- Árva csomagok listázása (függőségként telepített, de egyetlen csomag által sem igényelt csomagok):

`pacman --query --unrequired --deps --quiet`

- A tárolókban nem található telepített csomagok listázása:

`pacman --query --foreign`

- Lejárt csomagok listázása:

`pacman --query --upgrades`
