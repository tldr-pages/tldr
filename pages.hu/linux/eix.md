# eix

> Segédprogramok a helyi Gentoo csomagok kereséséhez. A helyi csomagtár frissítése a `eix-update` segítségével. További információ: <https://wiki.gentoo.org/wiki/Eix>.

- Csomag keresése:

`eix {{package_name}}`

- Telepített csomagok keresése:

`eix --installed {{package_name}}`

- Keresés a csomagleírásokban:

`eix --description "{{description}}"`

- Keresés a csomag licenc alapján:

`eix --license {{license}}`

- Eredmények kizárása a keresésből:

`eix --not --license {{license}}`
