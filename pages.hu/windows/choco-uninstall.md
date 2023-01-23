# choco uninstall

> Egy vagy több csomag eltávolítása a Chocolatey segítségével. További információ: <https://chocolatey.org/docs/commands-uninstall>.

- Egy vagy több, szóközzel elválasztott csomag eltávolítása:

`choco uninstall {{package(s)}}`

- Egy csomag egy adott verziójának eltávolítása:

`choco uninstall {{package}} --version {{version}}`

- Minden felszólítást automatikusan megerősít:

`choco uninstall {{package}} --yes`

- Az összes függőség eltávolítása az eltávolítás során:

`choco uninstall {{package}} --remove-dependencies`

- Az összes csomag eltávolítása:

`choco uninstall all`
