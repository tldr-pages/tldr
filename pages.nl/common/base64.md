# base32

> Codeer of decodeer een bestand of `stdin` van/naar Base32 naar `stdout`.
> Meer informatie: <https://manned.org/base32>.

- Encodeer een bestand:

`base32 {{pad/naar/bestand}}`

- Zet gecodeerde uitvoer naar een specifieke breedte (`0` schakelt het uit):

`base32 {{-w|--wrap}} {{0|76|...}} {{pad/naar/bestand}}`

- Decodeer een bestand:

`base32 {{-d|--decode}} {{pad/naar/bestand}}`

- Encodeer `stdin`:

`{{eencommando}} | base32`

- Decodeeer `stdin`:

`{{eencommando}} | base32 {{-d|--decode}}`
