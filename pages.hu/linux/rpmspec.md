# rpmspec

> RPM-specifikus fájl lekérdezése. További információ: <https://manned.org/rpmspec>.

- Az rpm spec fájlból generált bináris csomagok listázása:

`rpmspec --query {{path/to/rpm.spec}}`

- List all options for `--queryformat`:

`rpmspec --querytags`

- Egy rpm spec fájlból generált egyes bináris csomagok összefoglaló információinak lekérdezése:

`rpmspec --query --queryformat "{{%{name}: %{summary}\n}}" {{path/to/rpm.spec}}`

- Az rpm spec fájlból generált forráscsomagok lekérdezése:

`rpmspec --query --srpm {{path/to/rpm.spec}}`

- Az rpm spec fájl elemzése a `stdout`:

`rpmspec --parse {{path/to/rpm.spec}}`
