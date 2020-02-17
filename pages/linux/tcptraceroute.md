# tcptraceroute

> A traceroute implementation using TCP packets.
> More information: <https://github.com/mct/tcptraceroute>.

- Trace the route to a host:

`tcptraceroute {{host}}`

- Specify the destination port and packet length in bytes:

`tcptraceroute {{host}} {{destination_port}} {{packet_length}}`

- Specify the local source port and source address:

`tcptraceroute {{host}} -p {{source_port}} -s {{source_address}}`

- Set the initial and maximum TTL:

`tcptraceroute {{host}} -f {{first_ttl} -m {{max_ttl}}`

- Specify the wait time and number of probes for each hop:

`tcptraceroute {{host}} -w {{wait_time}} -q {{number_of_queries}}`

- Specify the interface:

`tcptraceroute {{host}} -i {{interface}}`
