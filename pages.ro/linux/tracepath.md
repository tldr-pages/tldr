# tracepath

> Trasați calea către o gazdă de rețea care descoperă MTU de-a lungul acestei căi.
> Mai multe informaţii: <https://manned.org/tracepath>

- O modalitate preferată de a urmări calea către o gazdă:

`tracepath -p {{33434}} {{host}}`

- Specificați portul inițial de destinație, util cu setările de firewall non-standard:

`tracepath -p {{destination_port}} {{host}} `

- Imprimați ambele nume de gazdă și adrese IP numerice:

`tracepath -b {{host}}`

- Specificați un TTL maxim (număr de hamei):

`tracepath -m {{max_hops}} {{host}}`

- Specificați lungimea inițială a pachetului (valorile implicite la 65535 pentru IPv4 și 128000 pentru IPv6):

`tracepath -l {{packet_length}} {{host}}`

- Utilizați numai adrese IPv6:

`tracepath -6 {{host}}`
