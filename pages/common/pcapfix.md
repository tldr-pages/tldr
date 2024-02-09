# pcapfix

> Repair damaged or corrupted `pcap` and `pcapng` files.
> More information: <https://f00l.de/pcapfix/>.

- Repair a `pcap`/`pcapng` file (Note: for `pcap` files, only the first 262144 bytes of each packet are scanned):

`pcapfix {{path/to/file.pcapng}}`

- Repair an entire `pcap` file:

`pcapfix --deep-scan {{path/to/file.pcap}}`

- Repair a `pcap`/`pcapng` file and write the repaired file to the specified location:

`pcapfix --outfile {{path/to/repaired.pcap}} {{path/to/file.pcap}}`

- Repair a `pcapng` file and treat it as a `pcapng` file, ignoring the automatic recognition:

`pcapfix --pcapng {{path/to/file.pcapng}}`

- Repair a file and show the process in detail:

`pcapfix --verbose {{path/to/file.pcap}}`
