# tracepath

> Trace the path to a network host discovering MTU along this path.
> More information: <https://manned.org/tracepath>.

- Trace the path to a host:

`tracepath {{host}}`

- Print numerical IP addresses only:

`tracepath -n {{host}}`

- Print both hostnames and numerical IP addresses:

`tracepath -b {{host}}`

- Specify a maximum TTL (number of hops):

`tracepath -m {{max_hops}} {{host}}`

- Specify the initial destination port, preferably 33434:

`tracepath -p {{destination_port}} {{host}} `

- Specify the initial packet length (defaults to 65535 for IPv4 and 128000 for IPv6):

`tracepath -l {{packet_length}} {{host}}`
