# tshark

> TShark is the CLI version of Wireshark which is a packet sniffer.
> Used to capture and analyze network traffic.
> More Information: <https://www.wireshark.org/docs/man-pages.tshark.html>.

- List Interfaces:

`tshark --list-interfaces`

- Write packet information to a file:

`tshark --interface {{interface_name}} -w {{path/to/file.pcap}}`

- Read the packet information from a file:

`tshark -r {{path/to/file.pcap}}`

- Capture a specific number of packets:

`tshark -c {{packet_count}}`

- Use capture filters to filter packets before they get analyzed:

`tshark -f {{"filter_name"}}`

- Use display filters to filter frames, ip packets or segments:

`tshark -Y {{"display_filter"}}`
