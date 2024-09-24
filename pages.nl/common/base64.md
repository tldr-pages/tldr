# base64

> Codeer of decodeer een bestand of `stdin` van/naar Base64 naar `stdout`.
> Meer informatie: <https://manned.org/base64>.

- Encodeer een bestand:

`base64 {{pad/naar/bestand}}`

- Zet gecodeerde uitvoer naar een specifieke breedte (`0` schakelt het uit):

`base64 {{-w|--wrap}} {{0|76|...}} {{pad/naar/bestand}}`

- Decodeer een bestand:

`base64 {{-d|--decode}} {{pad/naar/bestand}}`

- Encodeer `stdin`:

`{{eencommando}} | base64`

- Decodeeer `stdin`:

`{{eencommando}} | base64 {{-d|--decode}}`
