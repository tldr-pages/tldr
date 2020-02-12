# tcptraceroute

> A traceroute implementation using TCP packets.
> More information: <https://github.com/mct/tcptraceroute>.

- Trace the route to a host:

`tcptraceroute {{host}}`

- Specify destination port and packet length in bytes:

`tcptraceroute {{host}} {{destination_port}} {{packet_length}}`

- Specify local source port and source address:

`tcptraceroute {{host}} -p {{source_port}} -s {{source_address}}`

- Set initial and maximum TTL:

`tcptraceroute {{host}} -f {{first_ttl} -m {{max_ttl}}`

- Specify wait time and number of probes for each hop:

`tcptraceroute {{host}} -w {{wait_time}} -q {{number_of_queries}}`

- Specify interface with HTTP (port 80) as the destination port:

`tcptraceroute {{host}} -i {{interface}} http`
