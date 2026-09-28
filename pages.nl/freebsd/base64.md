# base64

> Codeer of decodeer een bestand of `stdin` naar/van base64, naar `stdout` of een ander bestand.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Codeer een bestand naar `stdout`:

`base64 {{[-i|--input]}} {{pad/naar/bestand}}`

- Codeer een bestand naar het opgegeven uitvoerbestand:

`base64 {{[-i|--input]}} {{pad/naar/invoerbestand}} {{[-o|--output]}} {{pad/naar/uitvoerbestand}}`

- Zet de breedte van de gecodeerde uitvoer op een specifieke waarde (`0` schakelt afbreken uit):

`base64 {{[-b|--break]}} {{0|76|...}} {{pad/naar/bestand}}`

- Decodeer een bestand naar `stdout`:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{pad/naar/bestand}}`

- Codeer van `stdin` naar `stdout`:

`{{commando}} | base64`

- Decodeer van `stdin` naar `stdout`:

`{{commando}} | base64 {{[-d|--decode]}}`
