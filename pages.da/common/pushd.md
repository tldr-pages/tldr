# pushd

> Tilføj en mappe til mappe-stakken, så den kan tilgås på et senere tidspunkt.
> Se `popd` for at skifte tilbage til den oprindelige mappe og `dirs` for at vise indholdet af mappe-stakken.
> Mere information: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Skift til mappe og tilføj den til mappe-stakken:

`pushd {{mappe}}`

- Byt om på første og anden mappe i mappe-stakken:

`pushd`

- Rotér mappe-stakken ved at gøre det femte element til det første i mappe-stakken:

`pushd +4`
