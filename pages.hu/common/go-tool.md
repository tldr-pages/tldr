# go tool

> Egy adott Go eszköz vagy parancs futtatása. Egy Go parancs önálló bináris programként történő futtatása, jellemzően hibakereséshez. További információ: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- Elérhető eszközök listája:

`go tool`

- A go link eszköz futtatása:

`go tool link {{path/to/main.o}}`

- Nyomtassa ki a végrehajtandó parancsot, de ne hajtsa végre (hasonlóan a `whereis`):

`go tool -n {{command}} {{arguments}}`

- A megadott eszköz dokumentációjának megjelenítése:

`go tool {{command}} --help`
