# hexdump

> Een ASCII, decimaal, hexadecimale, octale dump.
> Meer informatie: <https://manned.org/hexdump>.

- Toon de hexadecimale weergave van een bestand en vervang dubbele regels door '*':

`hexdump {{pad/naar/bestand}}`

- Toon de invoeroffset in hexadecimaal en zijn ASCII-weergave in twee kolommen:

`hexdump -C {{pad/naar/bestand}}`

- Geef de hexadecimale weergave van een bestand weer, maar interpreteer alleen n bytes van de invoer:

`hexdump -C -n{{aantal_bytes}} {{pad/naar/bestand}}`

- Vervang geen dubbele regels door '*':

`hexdump --no-squeezing {{pad/naar/bestand}}`
