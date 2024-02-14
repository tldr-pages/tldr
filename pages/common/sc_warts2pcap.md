# sc_warts2pcap

> Write packets included in `warts` object to a `pcap` file.
> This is only possible for tbit, sting and sniff.
> More information: <https://www.caida.org/catalog/software/scamper/>.

- Convert the data from several `warts` files into one `pcap` file:

`sc_warts2pcap -o {{path/to/output.pcap}} {{path/to/file1.warts path/to/file2.warts ...}}`

- Convert the data from a `warts` file into a `pcap` file and sort the packets by timestamp:

`sc_warts2pcap -s -o {{path/to/output.pcap}} {{path/to/file.warts}}`
