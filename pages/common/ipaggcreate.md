# ipaggcreate

> Produce aggregate statistics of TCP/IP dumps.
> More information: <https://read.seas.harvard.edu/~kohler/ipsumdump/aggcreateman.html>.

- Count the number of packets sent from each source address appearing in a pcap file:

`ipaggcreate -s {{path/to/file.pcap}}`

- Group and count packets read from network interface {{eth0}} by IP length:

`ipaggcreate -i {{eth0}} -l`

- Count the number of bytes sent between each address pair appearing in a pcap file:

`ipaggcreate --address-pairs -B {{path/to/file.pcap}}`
