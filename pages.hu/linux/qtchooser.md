# qtchooser

> A Qt fejlesztői bináris verziók közötti választásra használt wrapper. További információ: <https://manned.org/qtchooser>.

- Az elérhető Qt verziók listázása a konfigurációs fájlokból:

`qtchooser --list-versions`

- Környezeti információk nyomtatása:

`qtchooser --print-env`

- A megadott eszköz futtatása a megadott Qt verzióval:

`qtchooser --run-tool={{tool}} --qt={{version_name}}`

- Qt verzió bejegyzés hozzáadása, hogy választhasson:

`qtchooser --install {{version_name}} {{path/to/qmake}}`

- Az összes elérhető opció megjelenítése:

`qtchooser --help`
