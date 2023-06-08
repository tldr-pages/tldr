# babeld

> Routing-Daemon für Babel, der Firewall-ähnliche Filter benutzt.
> Weitere Informationen: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- Starte babeld von einer bestimmten Konfigurationsdatei:

`babeld -c {{path/to/babeld.conf}}`

- Starte babeld von mehreren Konfigurationsdateien (in der Reihenfolge des Einlesens):

`babeld -c {{path/to/ports.conf}} -c {{path/to/filters.conf}} -c {{path/to/interfaces.conf}}`

- Starte Babeld und versetze es danach in den Hintergrund:

`babeld -D`

- Starte babeld und übergeben einen Konfigurationsbefehl:

`babeld -C {{'redistribute metric 256'}}`

- Starte babeld und spezifiziere, auf welchen Schnittstellen gearbeitet werden soll:

`babeld {{eth0}} {{eth1}} {{wlan0}}`
