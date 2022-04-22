# dumpcap

> A network traffic dump tool.
> More information: <https://www.wireshark.org/docs/man-pages/dumpcap.html>.

- Get a list of available interfaces:

`dumpcap --list-interfaces`

- Start capturing packets on the first interface:

`dumpcap --interface 1`

- Start capturing packets on the first interface to a specific location:

`dumpcap --interface 1 -w {{path/to/output_file.pcapng}}`

- Start capturing packets on the first interface to a specific location and writing to a ring buffer with a max of 10 files of 500MB each:

`dumpcap --interface 1 -w {{path/to/output_file.pcapng}} --ring-buffer filesize:500000 --ring-buffer files:10`
