# babeld

> Routing-Daemon für Babel, der Firewall-ähnliche Filter benutzt.
> Weitere Informationen: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- Starte `babeld` mit einer bestimmten Konfigurationsdatei:

`babeld -c {{pfad/zu/babeld.conf}}`

- Starte `babeld` mit mehreren Konfigurationsdateien (in der Reihenfolge des Einlesens):

`babeld -c {{pfad/zu/ports.conf}} -c {{pfad/zu/filters.conf}} -c {{pfad/zu/interfaces.conf}}`

- Starte `babeld` als Daemon:

`babeld -D`

- Starte `babeld` und übergib einen Konfigurationsbefehl:

`babeld -C {{'redistribute metric 256'}}`

- Starte `babeld` und gib an, auf welchen Schnittstellen gearbeitet werden soll:

`babeld {{eth0}} {{eth1}} {{wlan0}}`
