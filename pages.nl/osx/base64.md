# base64

> Encodeer of decodeer een bestand of `stdin` van/naar base64, naar `stdout` of een ander bestand.
> Meer informatie: <https://keith.github.io/xcode-man-pages/bintrans.1>.

- Encodeer een bestand naar `stdout`:

`base64 {{[-i|--input]}} {{pad/naar/bestand}}`

- Encodeer een bestand naar het opgegeven uitvoerbestand:

`base64 {{[-i|--input]}} {{pad/naar/invoer_bestand}} {{[-o|--output]}} {{pad/naar/uitvoer_bestand}}`

- Wrap de uitvoer op een bepaalde breedte (`0` schakelt het uit):

`base64 {{[-b|--break]}} {{0|76|...}} {{pad/naar/bestand}}`

- Decodeer een bestand naar `stdout`:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{pad/naar/bestand}}`

- Encodeer van `stdin` naar `stdout`:

`{{commando}} | base64`

- Decodeer vanaf `stdin` naar `stdout`:

`{{commando}} | base64 {{[-d|--decode]}}`
