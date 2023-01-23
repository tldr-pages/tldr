# ftp

> Eszközök a szerverrel való interakcióhoz a File Transfer Protocol-on keresztül. További információ: <https://manned.org/ftp>.

- Csatlakozás egy FTP-kiszolgálóhoz:

`ftp {{ftp.example.com}}`

- Csatlakozás egy FTP-kiszolgálóhoz, megadva annak IP-címét és portját:

`ftp {{ip_address}} {{port}}`

- Váltson bináris átviteli módra (grafikák, tömörített fájlok stb.):

`binary`

- Több fájl átvitele anélkül, hogy minden egyes fájlnál megerősítést kérne:

`prompt off`

- Több fájl letöltése (glob kifejezés):

`mget {{*.png}}`

- Több fájl feltöltése (glob kifejezés):

`mput {{*.zip}}`

- Több fájl törlése a távoli kiszolgálón:

`mdelete {{*.txt}}`

- Fájl átnevezése a távoli kiszolgálón:

`rename {{original_filename}} {{new_filename}}`
