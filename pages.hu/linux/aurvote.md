# aurvote

> Szavazzon az Arch User Repository-ban lévő csomagokra. A szavazáshoz a `~/.config/aurvote` fájlnak léteznie kell, és tartalmaznia kell az AUR hitelesítő adatait. További információ: <https://github.com/archlinuxfr/aurvote>.

- Interaktívan hozza létre a `~/.config/aurvote` fájlt, amely tartalmazza az AUR felhasználónevét és jelszavát:

`aurvote --configure`

- Szavazzon egy vagy több AUR csomagra:

`aurvote {{package1 package2 ...}}`

- Egy vagy több AUR-csomag visszavonása:

`aurvote --unvote {{package1 package2 ...}}`

- Ellenőrizze, hogy egy vagy több AUR csomagot már megszavaztak-e:

`aurvote --check {{package1 package2 ...}}`

- A `aurvote` súgójának megjelenítése:

`aurvote --help`
