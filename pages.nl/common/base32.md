# base32

> Codeer of decodeer een bestand of `stdin` van/naar Base32 naar `stdout`.
> Meer informatie: <https://www.gnu.org/software/coreutils/base32>.

- Encodeer een bestand:

`base32 {{pad/naar/bestand}}`

- Zet gecodeerde uitvoer naar een specifieke breedte (`0` schakelt het uit):

`base32 --wrap {{0|76|...}} {{path/to/file}}`

- Decodeer een bestand:

`base32 --decode {{pad/naar/bestand}}`

- Encodeer `stdin`:

`{{somecommand}} | base32`

- Decodeeer `stdin`:

`{{somecommand}} | base32 --decode`
