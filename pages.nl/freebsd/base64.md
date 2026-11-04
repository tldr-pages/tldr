# base64

> Codeer of decodeer een bestand of `stdin` naar/van base64, naar `stdout`.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Codeer een bestand naar `stdout`:

`base64 {{pad/naar/bestand}}`

- Zet de breedte van de gecodeerde uitvoer op een specifieke kolombreedte (`0` schakelt afbreken uit):

`base64 -w {{0|76|...}} {{pad/naar/bestand}}`

- Decodeer een bestand naar `stdout`:

`base64 -d {{pad/naar/bestand}}`

- Codeer van `stdin` naar `stdout`:

`{{commando}} | base64`

- Decodeer van `stdin` naar `stdout`:

`{{commando}} | base64 -d`
