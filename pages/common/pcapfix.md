# pcapfix

> Repair damaged or corrupted PCAP and PcapNG files.
> More information: <https://f00l.de/pcapfix/>.

- Repair a PCAP/PCapNG file (Note: for PCAP files, only the first 262144 bytes of each packet are scanned):

`pcapfix {{path/to/file.pcapng}}`

- Repair an entire PCAP file:

`pcapfix --deep-scan {{path/to/file.pcap}}`

- Repair a PCAP/PcapNG file and write the repaired file to the specified location:

`pcapfix --outfile {{path/to/repaired.pcap}} {{path/to/file.pcap}}`

- Treat the specified file as a PcapNG file, ignoring automatic recognition:

`pcapfix --pcapng {{path/to/file.pcapng}}`

- Repair a file and show the process in detail:

`pcapfix --verbose {{path/to/file.pcap}}`
