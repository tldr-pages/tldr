# ps

> Információ a futó folyamatokról. További információ: <https://manned.org/ps>.

- Az összes futó folyamat listázása:

`ps aux`

- Az összes futó folyamat listázása a teljes parancssorral együtt:

`ps auxww`

- Olyan folyamat keresése, amely megfelel egy karakterláncnak:

`ps aux | grep {{string}}`

- Az aktuális felhasználó összes folyamatának listázása extra teljes formátumban:

`ps --user $(id -u) -F`

- Az aktuális felhasználó összes folyamatának faként történő listázása:

`ps --user $(id -u) f`

- Egy folyamat szülő PID-jének lekérdezése:

`ps -o ppid= -p {{pid}}`

- A folyamatok rendezése memóriafogyasztás szerint:

`ps --sort size`
