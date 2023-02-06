# mount

> Hálózati fájlrendszer (NFS) hálózati megosztások csatlakoztatása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/mount>.

- Csatlakoztasson egy megosztást a "Z" meghajtó betűjellel:

`mount \\{{computer_name}}\{{share_name}} {{Z:}}`

- Megosztás csatlakoztatása a következő elérhető meghajtóbetűre:

`mount \\{{computer_name}}\{{share_name}} *`

- Megosztás csatlakoztatása másodpercben megadott olvasási időkorlátozással (alapértelmezett érték 0,8, lehet 0,9 vagy 1-től 60-ig):

`mount -o timeout={{seconds}} \\{{computer_name}}\{{share_name}} {{Z:}}`

- Megosztás csatlakoztatása és legfeljebb 10-szeri újbóli próbálkozás, ha nem sikerül:

`mount -o retry={{retries}} \\{{computer_name}}\{{share_name}} {{Z:}}`

- Megosztás csatlakoztatása kényszerített nagy- és kisbetű érzékenységgel:

`mount -o casesensitive \\{{computer_name}}\{{share_name}} {{Z:}}`

- Megosztás csatlakoztatása névtelen felhasználóként:

`mount -o anon \\{{computer_name}}\{{share_name}} {{Z:}}`

- Megosztás csatlakoztatása egy adott csatlakoztatási típussal:

`mount -o mtype={{soft|hard}} \\{{computer_name}}\{{share_name}} {{Z:}}`
