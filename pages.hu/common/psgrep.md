# psgrep

> A futó folyamatok keresése a `grep` segítségével. További információ: [https://jvz.github.io/psgrep.](https://jvz.github.io/psgrep)

- Egy adott karakterláncot tartalmazó folyamatsorok keresése:

`psgrep {{process_name}}`

- Egy adott karakterláncot tartalmazó folyamatsorok keresése, a fejlécek kivételével:

`psgrep -n {{process_name}}`

- Keresés egyszerűsített formátumban (PID, felhasználó, parancs):

`psgrep -s {{process_name}}`
