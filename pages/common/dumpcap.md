# dumpcap

> A network traffic dump tool.
> More information: <https://www.wireshark.org/docs/man-pages/dumpcap.html>.

- Display available interfaces:

`dumpcap {{[-D|--list-interfaces]}}`

- Capture packets on a specific interface:

`dumpcap {{[-i|--interface]}} {{1}}`

- Capture packets to a specific location:

`dumpcap {{[-i|--interface]}} {{1}} -w {{path/to/output_file.pcapng}}`

- Write to a ring buffer with a specific max file limit of a specific size:

`dumpcap {{[-i|--interface]}} {{1}} -w {{path/to/output_file.pcapng}} {{[-b|--ring-buffer]}} filesize:{{500000}} {{[-b|--ring-buffer]}} files:{{10}}`
