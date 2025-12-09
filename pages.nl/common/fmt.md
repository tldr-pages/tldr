# fmt

> Herformatteer een tekstbestand door de alinea's samen te voegen en de regelbreedte te beperken tot een aantal tekens (standaard 75).
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html>.

- Herformatteer een bestand:

`fmt {{pad/naar/bestand}}`

- Herformatteer een bestand met uitvoerregels van (hoogstens) `n` tekens:

`fmt {{[-w|--width]}} {{n}} {{pad/naar/bestand}}`

- Herformatteer een bestand zonder regels die korter zijn dan de opgegeven breedte samen te voegen:

`fmt {{[-s|--split-only]}} {{pad/naar/bestand}}`

- Herformatteer een bestand met uniforme spatiëring (1 spatie tussen woorden en 2 spaties tussen alinea's):

`fmt {{[-u|--uniform-spacing]}} {{pad/naar/bestand}}`
