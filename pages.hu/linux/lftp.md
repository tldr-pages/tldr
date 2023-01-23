# lftp

> Kifinomult fájlátviteli program. További információ: <https://lftp.yar.ru/lftp-man.html>.

- Csatlakozás egy FTP-kiszolgálóhoz:

`lftp {{ftp.example.com}}`

- Több fájl letöltése (glob kifejezés):

`mget {{path/to/*.png}}`

- Több fájl feltöltése (glob kifejezés):

`mput {{path/to/*.zip}}`

- Több fájl törlése a távoli kiszolgálón:

`mrm {{path/to/*.txt}}`

- Fájl átnevezése a távoli kiszolgálón:

`mv {{original_filename}} {{new_filename}}`

- Teljes könyvtár letöltése vagy frissítése:

`mirror {{path/to/remote_dir}} {{path/to/local_output_dir}}`

- Teljes könyvtár feltöltése vagy frissítése:

`mirror -R {{path/to/local_dir}} {{path/to/remote_output_dir}}`
