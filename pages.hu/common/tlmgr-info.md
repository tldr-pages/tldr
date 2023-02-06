# tlmgr info

> A TeX Live csomagokkal kapcsolatos információk megjelenítése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Az összes elérhető TeX Live csomag listázása, a telepítettek előnyben részesítése a `i` címmel:

`tlmgr info`

- Az összes elérhető gyűjtemény felsorolása:

`tlmgr info collections`

- List all available schemes:

`tlmgr info scheme`

- Információk megjelenítése egy adott csomagról:

`tlmgr info {{package_name}}`

- Egy adott csomagban található összes fájl listázása:

`tlmgr info {{package_name}} --list`

- Az összes telepített csomag listája:

`tlmgr info --only-installed`

- Csak bizonyos információk megjelenítése egy csomagról:

`tlmgr info {{package_name}} --data "{{name}},{{category}},{{installed}},{{size}},{{depends}},..."`

- Az összes rendelkezésre álló csomag JSON kódolt tömbként történő kiírása:

`tlmgr info --json`
