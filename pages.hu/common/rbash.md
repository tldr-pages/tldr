# rbash

> Korlátozott Bash shell, egyenértékű a `bash --restricted`-val . Nem engedélyezi többek között a munkakönyvtár megváltoztatását, a parancsok kimenetének átirányítását vagy a környezeti változók módosítását. Lásd még `histexpand` az előzmények bővítéséhez. További információ: <https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell>.

- Interaktív shell munkamenet indítása:

`rbash`

- Egy parancs végrehajtása, majd kilépés:

`rbash -c "{{command}}"`

- Szkript végrehajtása:

`rbash {{path/to/script.sh}}`

- Szkript végrehajtása, minden egyes parancsot a végrehajtás előtt kinyomtatva:

`rbash -x {{path/to/script.sh}}`

- Parancsok végrehajtása egy szkriptből, az első hiba esetén megállítva:

`rbash -e {{path/to/script.sh}}`

- Parancsok beolvasása és végrehajtása a `stdin` oldalról:

`rbash -s`
