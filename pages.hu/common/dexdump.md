# dexdump

> Android DEX fájlokra vonatkozó információk megjelenítése. További információ: <https://manned.org/dexdump>.

- Osztályok és metódusok kivonása egy APK fájlból:

`dexdump {{path/to/file.apk}}`

- Az APK-fájlban található DEX-fájlok fejlécinformációinak megjelenítése:

`dexdump -f {{path/to/file.apk}}`

- A futtatható részek szétszerelt kimenetének megjelenítése:

`dexdump -d {{path/to/file.apk}}`

- Az eredmények kiadása egy fájlba:

`dexdump -o {{path/to/file}} {{path/to/file.apk}}`
