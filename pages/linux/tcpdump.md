# tcpdump

> TCP network traffic analyzer.
> More information: <https://www.tcpdump.org/manpages/tcpdump.1.html>.

- Capture traffic on specific interface:

`tcpdump --interface={{ens160}}`

- Capture ip host-specific packets:

`tcpdump --interface={{ens160}} --count={{5}} {{140.240.61.21}}`

- Capture packets on a specific port:

`tcpdump --interface={{ens160}} {{port}}`

- Write packets to a file:

`tcpdump --count={{5}} -w {{path/to/file.pcap}} --interface={{interface}}`

- Capture packets from a specific protocol:

`tcpdump --interface={{interface}} --count={{5}} -nn tcp`

- Filter tcpdump packets from specific source & dest host:

`tcpdump {{100.10.8.121}}`

- Rotate tcpdump packets:

`tcpdump --interface={{interface}} -w {{path/to/file.pcap}} -W {{48}} -G {{300}} -C {{100}}`
