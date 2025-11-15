# hexdump

> Een ASCII, decimale, hexadecimale, octale dump.
> Meer informatie: <https://manned.org/hexdump>.

- Druk de hexadecimale weergave van een bestand af, waarbij dubbele regels worden vervangen door '*':

`hexdump {{pad/naar/bestand}}`

- Toon de invoer offset in hexadecimaal en zijn ASCII representatie in twee kolommen:

`hexdump {{[-C|--canonical]}} {{pad/naar/bestand}}`

- Geef de hexadecimale weergave van een bestand weer, maar interpreteer alleen n bytes van de invoer:

`hexdump {{[-C|--canonical]}} {{[-n|--lengte]}} {{aantal_bytes}} {{pad/naar/bestand}}`

- Vervang dubbele regels niet door '*':

`hexdump {{[-v|--no-squeezing]}} {{pad/naar/bestand}}`
