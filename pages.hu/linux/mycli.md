# mycli

> CLI a MySQL, MariaDB és Percona számára automatikus kitöltéssel és szintaxis-kiemeléssel. További információ: <https://manned.org/mycli>.

- Csatlakozás egy adatbázishoz az aktuálisan bejelentkezett felhasználóval:

`mycli {{database_name}}`

- Csatlakozás egy adatbázishoz a megadott felhasználóval:

`mycli -u {{user}} {{database_name}}`

- Csatlakozás a megadott állomáson lévő adatbázishoz a megadott felhasználóval:

`mycli -u {{user}} -h {{host}} {{database_name}}`
