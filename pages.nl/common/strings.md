# strings

> Vind printbare strings in een object bestand of binary.
> Meer informatie: <https://manned.org/strings>.

- Toon alle strings in een binary:

`strings {{pad/naar/bestand}}`

- Limiteer resultaten van strings met minimaal n karakters lang:

`strings {{[-n|--bytes]}} {{n}} {{pad/naar/bestand}}`

- Prefix ieder resultaat met de offset in het bestand:

`strings {{[-t|--radix]}} d {{pad/naar/bestand}}`

- Prefix ieder resultaat met de offset in het bestand als hexadecimaal:

`strings {{[-t|--radix]}} x {{pad/naar/bestand}}`
