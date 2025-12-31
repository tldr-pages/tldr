# netselect

> Speed test for choosing a fast network server.
> More information: <https://manned.org/netselect>.

- Choose the server with the lowest latency:

`sudo netselect {{host_1 host_2 ...}}`

- Display nameserver resolution and statistics:

`sudo netselect -vv {{host_1 host_2 ...}}`

- Define maximum TTL (time to live):

`sudo netselect -m {{10}} {{host_1 host_2 ...}}`

- Print `n` fastest servers among the hosts:

`sudo netselect -s {{n}} {{host_1 host_2 host_3 ...}}`

- Display help:

`netselect`
