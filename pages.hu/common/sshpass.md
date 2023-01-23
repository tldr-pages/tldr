# sshpass

> Egy ssh jelszó szolgáltató. Úgy működik, hogy létrehoz egy TTY-t, betáplálja a jelszót, majd átirányítja a `stdin` az ssh munkamenetre. További információ: <https://manned.org/sshpass>.

- Csatlakozás egy távoli kiszolgálóhoz egy fájlleírón (ebben az esetben `stdin`) megadott jelszóval:

`sshpass -d {{0}} ssh {{user}}@{{hostname}}`

- Csatlakozás egy távoli kiszolgálóhoz a megadott jelszóval, és az ismeretlen ssh kulcsok automatikus elfogadása:

`sshpass -p {{password}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}}`

- Csatlakozás egy távoli kiszolgálóhoz egy fájl első sorát jelszóként használva, ismeretlen ssh kulcsok automatikus elfogadása, és egy parancs indítása:

`sshpass -f {{path/to/file}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} "{{command}}"`
