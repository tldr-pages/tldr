# od

> Toon bestandsinhoud in octale, decimale of hexadecimale notatie.
> Toon optioneel de byte-offsets en/of de afdrukbare weergave voor elke regel.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>.

- Toon bestand met de standaardinstellingen: octale notatie, 8 bytes per regel, byte-offsets in octale notatie en dubbele regels vervangen door `*`:

`od {{pad/naar/bestand}}`

- Toon bestand in uitgebreide modus, d.w.z. zonder dubbele regels te vervangen door `*`:

`od -v {{pad/naar/bestand}}`

- Toon bestand in hexadecimale notatie (2-byte eenheden), met byte-offsets in decimale notatie:

`od --format={{x}} --address-radix={{d}} -v {{pad/naar/bestand}}`

- Toon bestand in hexadecimale notatie (1-byte eenheden) en 4 bytes per regel:

`od --format={{x1}} --width={{4}} -v {{pad/naar/bestand}}`

- Toon bestand in hexadecimale notatie samen met de tekenweergave, en toon geen byte-offsets:

`od --format={{xz}} --address-radix={{n}} -v {{pad/naar/bestand}}`

- Lees slechts 100 bytes van een bestand vanaf de 500ste byte:

`od --read-bytes 100 --skip-bytes=500 -v {{pad/naar/bestand}}`
