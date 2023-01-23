# pamac

> A GUI csomagkezelő pamac parancssori segédprogramja. Ha nem látod az AUR csomagokat, engedélyezd a `/etc/pamac.conf` vagy a GUI-ban. További információ: <https://wiki.manjaro.org/index.php/Pamac>.

- Új csomag telepítése:

`pamac install {{package_name}}`

- Egy csomag és annak már nem szükséges függőségei (árvák) eltávolítása:

`pamac remove --orphans {{package_name}}`

- Keressen egy csomagot a csomagadatbázisban:

`pamac search {{package_name}}`

- Telepített csomagok listázása:

`pamac list --installed`

- Csomagfrissítések keresése:

`pamac checkupdates`

- Az összes csomag frissítése:

`pamac upgrade`
