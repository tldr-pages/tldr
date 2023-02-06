# mysqlbinlog

> Segédprogram a MySQL bináris naplófájlok feldolgozásához. További információ: <https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html>.

- Események megjelenítése egy adott bináris naplófájlból:

`mysqlbinlog {{path/to/binlog}}`

- Egy adott adatbázis bináris naplójának bejegyzéseinek megjelenítése:

`mysqlbinlog --database {{database_name}} {{path/to/binlog}}`

- Bizonyos dátumok közötti események megjelenítése egy bináris naplóból:

`mysqlbinlog --start-datetime='{{2022-01-01 01:00:00}}' --stop-datetime='{{2022-02-01 01:00:00}}' {{path/to/binlog}}`

- Események megjelenítése egy bináris naplóból meghatározott pozíciók között:

`mysqlbinlog --start-position={{100}} --stop-position={{200}} {{path/to/binlog}}`

- A megadott állomáson lévő MySQL-kiszolgáló bináris naplójának megjelenítése:

`mysqlbinlog --host={{hostname}} {{path/to/binlog}}`
