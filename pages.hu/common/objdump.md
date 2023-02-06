# objdump

> Az objektumfájlokra vonatkozó információk megtekintése. További információ: <https://manned.org/objdump>.

- A fájl fejléc információinak megjelenítése:

`objdump -f {{binary}}`

- A futtatható szakaszok szétszerelt kimeneteinek megjelenítése:

`objdump -d {{binary}}`

- A futtatható szakaszok szétszerelt kimenete intel szintaxisban:

`objdump -M intel -d {{binary}}`

- Az összes szakasz teljes bináris hexdumpjának megjelenítése:

`objdump -s {{binary}}`
