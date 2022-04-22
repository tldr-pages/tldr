# dumpcap - Dump network traffic

> A network traffic dump tool.
> More information: <https://www.wireshark.org/docs/man-pages/dumpcap.html>.

- Get a list of available interfaces:

`dumpcap -D`

- Start capturing packets on the first interface:

`dumpcap -i 1`

- Start capturing packets on the first interface to a specific location:

`dumpcap -i 1 -w path/to/write/file/to.pcapng`

- Start capturing packets on the first interface to a specific location and writing to a ring buffer with a max of 10 files of 500MB each:

`dumpcap -i 1 -w path/to/write/file/to.pcapng -b filesize:500000 -b files:10`
