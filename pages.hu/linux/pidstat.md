# pidstat

> A rendszererőforrás-használat megjelenítése, beleértve a CPU, memória, IO stb. használatát. További információ: <https://manned.org/pidstat>.

- CPU-statisztikák megjelenítése 2 másodperces időközönként 10 alkalommal:

`pidstat {{2}} {{10}}`

- Oldalhibák és memóriahasználat megjelenítése:

`pidstat -r`

- Be- és kimeneti felhasználás megjelenítése folyamatazonosítónként:

`pidstat -d`

- Egy adott PID-re vonatkozó információk megjelenítése:

`pidstat -p {{PID}}`

- Mutasd a memóriastatisztikákat minden olyan folyamatra, amelynek a parancsnevében szerepel a "fox" vagy a "bird":

`pidstat -C "{{fox|bird}}" -r -p ALL`
