# smbclient

> FTP-szerű kliens a szerverek SMB/CIFS erőforrásainak eléréséhez. További információ: <https://manned.org/smbclient>.

- Csatlakozás egy megosztáshoz (a felhasználónak jelszót kell kérnie; `exit` a munkamenet kilépéséhez):

`smbclient {{//server/share}}`

- Csatlakozás más felhasználónévvel:

`smbclient {{//server/share}} --user {{username}}`

- Csatlakozás másik munkacsoporttal:

`smbclient {{//server/share}} --workgroup {{domain}} --user {{username}}`

- Csatlakozás felhasználónévvel és jelszóval:

`smbclient {{//server/share}} --user {{username%password}}`

- Fájl letöltése a kiszolgálóról:

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "get {{file.txt}}"`

- Fájl feltöltése a kiszolgálóra:

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "put {{file.txt}}"`

- A kiszolgáló megosztásainak névtelen listázása:

`smbclient --list={{server}} --no-pass`
