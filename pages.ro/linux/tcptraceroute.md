# tcptraceroute

> O implementare traceroute folosind pachete TCP.
> Mai multe informaţii: <https://github.com/mct/tcptraceroute>

- Trasați traseul către o gazdă:

`tcptraceroute {{host}}`

- Specificați portul de destinație și lungimea pachetului în octeți:

`tcptraceroute {{host}} {{destination_port}} {{packet_length}}`

- Specificați portul sursă locală și adresa sursă:

`tcptraceroute {{host}} -p {{source_port}} -s {{source_address}}`

- Setați primul și maxim TTL:

`tcptraceroute {{host}} -f {{first_ttl}} -m {{max_ttl}}`

- Specificați timpul de așteptare și numărul de interogări pe hamei:

`tcptraceroute {{host}} -w {{wait_time}} -q {{number_of_queries}}`

- Specificați interfața:

`tcptraceroute {{host}} -i {{interface}}`
