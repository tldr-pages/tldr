# ntpq

> A Network Time Protocol (NTP) démon lekérdezése. További információ: <https://www.eecis.udel.edu/~mills/ntp/html/ntpq.html>.

- Indítsa el a `ntpq` oldalt interaktív módban:

`ntpq --interactive`

- Az NTP-partnerek listájának kinyomtatása:

`ntpq --peers`

- Az NTP-partnerek listájának nyomtatása anélkül, hogy az IP-címekből feloldaná a hostneveket:

`ntpq --numeric --peers`

- A `ntpq` használata hibakeresési módban:

`ntpq --debug-level`

- NTP rendszerváltozók értékeinek nyomtatása:

`ntpq --command={{rv}}`
