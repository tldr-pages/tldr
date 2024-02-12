# babeld

> Routing daemon for Babel which uses firewall-style filters.
> More information: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- Start the daemon with one or more [c]onfiguration files (read in order):

`babeld -c {{path/to/ports.conf}} -c {{path/to/filters.conf}} -c {{path/to/interfaces.conf}}`

- [D]eamonize after startup:

`babeld -D`

- Specify a [C]onfiguration command:

`babeld -C {{'redistribute metric 256'}}`

- Specify on which interfaces to operate:

`babeld {{eth0}} {{eth1}} {{wlan0}}`
