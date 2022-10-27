# ahost

> DNS lookup utility to display the A or AAAA record linked with a hostname or IP address.
> More information: <https://manned.org/ahost>.

- Print an `A` or `AAAA` record associated with a hostname or IP address:

`ahost {{example.com}}`

- Display some extra debugging output:

`ahost -d {{example.com}}`

- Display the record with a specified type:

`ahost -t {{a|aaaa|u}} {{example.com}}`
