# ego

> A Funtoo hivatalos rendszerszemélyiség-kezelő eszköze. További információ: <https://funtoo-ego.readthedocs.io/en/develop/>.

- Szinkronizálja a Portage fát:

`ego sync`

- A bootloader konfigurációjának frissítése:

`ego boot update`

- Egy Funtoo wiki oldal név szerinti olvasása:

`ego doc {{wiki_page}}`

- Jelenlegi profil nyomtatása:

`ego profile show`

- Mix-ins engedélyezése/letiltása:

`ego profile mix-in +{{gnome}} -{{kde-plasma-5}}`

- Funtoo hibák lekérdezése egy megadott csomaghoz kapcsolódóan:

`ego query bug {{package}}`
