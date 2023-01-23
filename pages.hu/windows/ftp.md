# ftp

> Interaktív fájlátvitel egy helyi és egy távoli FTP-kiszolgáló között. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Csatlakozás egy távoli FTP-kiszolgálóhoz interaktívan:

`ftp {{host}}`

- Jelentkezzen be névtelen felhasználóként:

`ftp -A {{host}}`

- Az automatikus bejelentkezés kikapcsolása az első csatlakozáskor:

`ftp -n {{host}}`

- FTP-parancsok listáját tartalmazó fájl futtatása:

`ftp -s:{{path/to/file}} {{host}}`

- Több fájl letöltése (glob kifejezés):

`mget {{*.png}}`

- Több fájl feltöltése (glob kifejezés):

`mput {{*.zip}}`

- Több fájl törlése a távoli kiszolgálón:

`mdelete {{*.txt}}`

- Részletes súgó megjelenítése:

`ftp --help`
