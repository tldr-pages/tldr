# sngrep

> Tool for displaying SIP calls message flows from terminal.
> More information: <https://github.com/irontec/sngrep>.

- Visualize SIP packets from a PCAP file:

`sngrep -I {{path/to/file.pcap}}`

- Visualize only dialogs starting with INVITE packets with RTP packets from a PCAP file:

`sngrep -crI {{path/to/file.pcap}}`

- Real-time interface with only dialogs starting with INVITE packets with RTP packets:

`sngrep -cr`

- Only capture packets without interface to a file:

`sngrep -NO {{path/to/file.pcap}}`
