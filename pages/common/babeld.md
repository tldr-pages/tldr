# babeld

> Routing daemon for Babel which uses firewall-style filters.
> More information: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- Start `babeld` with a specific [c]onfiguration file:

`babeld -c {{path/to/babeld.conf}}`

- Start `babeld` with multiple [c]onfiguration files (read in order):

`babeld -c {{path/to/ports.conf}} -c {{path/to/filters.conf}} -c {{path/to/interfaces.conf}}`

- Start `babeld` and [D]aemonise afterwards:

`babeld -D`

- Start `babeld` and pass a [C]onfiguration command:

`babeld -C {{'redistribute metric 256'}}`

- Start `babeld` and specify on which interfaces to operate:

`babeld {{eth0}} {{eth1}} {{wlan0}}`
