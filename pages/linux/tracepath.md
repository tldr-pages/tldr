# tracepath

> Trace path to a network host discovering MTU along this path.
> More information: <https://manned.org/tracepath>.

- Trace the path to a host:

`tracepath {{host}}`

- Print numerical IP addresses only:

`tracepath -n {{host}}`

- Print both hostnames and numerical IP addresses:

`tracepath -b {{host}}`

- Specify maximum TTL (number of hops):

`tracepath -m {{max_hops}} {{host}}`

- Specify the initial destination port:

`tracepath -p {{destination_port}} {{host}} `

- Specify the initial packet length:

`tracepath -l {{packet_length}} {{host}}`
