# strings

> Vind printbare strings in een object bestand of binary.
> Meer informatie: <https://manned.org/strings>.

- Print alle strings in een binary:

`strings {{pad/naar/bestand}}`

- Limiteer resultaten van strings met minimaal n karakters lang:

`strings -n {{n}} {{pad/naar/bestand}}`

- Prefix ieder resultaat met de offset in het bestand:

`strings -t d {{pad/naar/bestand}}`

- Prefix ieder resultaat met de offset in het bestand als hexadecimaal:

`strings -t x {{pad/naar/bestand}}`
