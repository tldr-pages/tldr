# mmdblookup

> A utility to look up an IP address in a MaxMind DB file.
> More information: <https://maxmind.github.io/libmaxminddb/mmdblookup.html>.

- Look up an IP address in the specified MaxMind DB file:

`mmdblookup {{[-f|--file]}} {{path/to/dataset.mmdb}} {{[-i|--ip]}} {{8.8.8.8}}`

- Look up a subset of data for an IP address in the specified MaxMind DB file:

`mmdblookup {{[-f|--file]}} {{path/to/dataset.mmdb}} {{[-i|--ip]}} {{8.8.8.8}} {{country iso_code}}`

- Display help:

`mmdblookup {{[-h|--help]}}`

- Display version:

`mmdblookup --version`
