# guix package

> A Guix csomagok telepítése, frissítése és eltávolítása, illetve a korábbi konfigurációk visszaállítása. További információ: <https://guix.gnu.org/manual/html_node/Invoking-guix-package.html>.

- Új csomag telepítése:

`guix package -i {{package_name}}`

- Csomag eltávolítása:

`guix package -r {{package_name}}`

- Keresés a csomagadatbázisban egy reguláris kifejezésre:

`guix package -s "{{search_pattern}}"`

- Telepített csomagok listázása:

`guix package -I`

- Generációk listázása:

`guix package -l`

- Visszaállítás az előző generációra:

`guix package --roll-back`
