# mycli

> Parancssori kliens a MySQL-hez, amely képes automatikus kiegészítésre és szintaxis-kiemelésre. További információ: <https://mycli.net>.

- Csatlakozás egy helyi adatbázishoz a 3306-os porton, az aktuális felhasználó felhasználónevével:

`mycli {{database_name}}`

- Csatlakozás egy adatbázishoz (a felhasználónak jelszót kell megadnia):

`mycli -u {{username}} {{database_name}}`

- Csatlakozás egy másik állomáson lévő adatbázishoz:

`mycli -h {{database_host}} -P {{port}} -u {{username}} {{database_name}}`
