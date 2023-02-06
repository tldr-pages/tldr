# while

> Egyszerű kagylóhurok. További információ: <https://manned.org/while>.

- A `stdin` beolvasása és egy művelet végrehajtása minden soron:

`while read line; do echo "$line"; done`

- Minden másodpercben egyszer örökké végrehajt egy parancsot:

`while :; do {{command}}; sleep 1; done`
