# od

> Toon bestandsinhoud in octale, decimale of hexadecimale notatie.
> Toon optioneel de byte-offsets en/of de afdrukbare weergave voor elke regel.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>.

- Toon bestand met de standaardinstellingen: octale notatie, 8 bytes per regel, byte-offsets in octale notatie en dubbele regels vervangen door `*`:

`od {{pad/naar/bestand}}`

- Toon bestand in uitgebreide modus, d.w.z. zonder dubbele regels te vervangen door `*`:

`od {{[-v|--output-duplicates]}} {{pad/naar/bestand}}`

- Toon bestand in hexadecimale notatie (2-byte eenheden), met byte-offsets in decimale notatie:

`od {{[-t|--format]}} {{x}} {{[-A|--address-radix]}} {{d}} {{[-v|--output-duplicates]}} {{pad/naar/bestand}}`

- Toon bestand in hexadecimale notatie (1-byte eenheden) en 4 bytes per regel:

`od {{[-t|--format]}} {{x1}} {{[-w|--width=]}}4 {{[-v|--output-duplicates]}} {{pad/naar/bestand}}`

- Toon bestand in hexadecimale notatie samen met de tekenweergave, en toon geen byte-offsets:

`od {{[-t|--format]}} {{xz}} {{[-A|--address-radix]}} {{n}} {{[-v|--output-duplicates]}} {{pad/naar/bestand}}`

- Lees slechts 100 bytes van een bestand vanaf de 500ste byte:

`od {{[-N|--read-bytes]}} 100 {{[-j|--skip-bytes]}} 500 {{[-v|--output-duplicates]}} {{pad/naar/bestand}}`
