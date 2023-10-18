# nping

> Network packet generation tool/ping utility.
> More information: <https://nmap.org/nping/>.

- Ping a specified host using ICMP if the user is allowed to, otherwise using TCP:

`nping {{example.com}}`

- Ping a specified host using ICMP assuming that the user is allowed to do so:

`nping --icmp --privileged {{example.com}}`

- Ping a specified host using UDP:

`nping --udp {{example.com}}`

- Ping a specified host on a given port using TCP:

`nping --tcp --dest-port {{443}} {{example.com}}`

- Ping a certain number of times:

`nping --count {{10}} {{example.com}}`

- Wait a certain amount of time between each ping:

`nping --delay {{5s}} {{example.com}}`

- Send the request over a specified interface:

`nping --interface {{eth0}} {{example.com}}`

- Set the Reserved/Evil bit in sent packets:

`nping --evil {{example.com}}`
