# base64

> Encodeer of decodeer een bestand of `stdin` van/naar Base64 naar `stdout`.
> Meer informatie: <https://www.gnu.org/software/coreutils/base64>.

- Encodeer een bestand:

`base64 {{bestandsnaam}}`

- Decodeer een bestand:

`base64 --decode {{bestandsnaam}}`

- Encodeer `stdin`:

`{{eencommando}} | base64`

- Decodeer `stdin`:

`{{eencommando}} | base64 --decode`
