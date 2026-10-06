# xxd

> Maak een hexadecimale representatie (hexdump) van een binair bestand, of andersom.
> Zie ook: `hexyl`, `od`, `hexdump`.
> Meer informatie: <https://manned.org/xxd>.

- Genereer een hexdump van een binair bestand en toon de uitvoer:

`xxd {{invoerbestand}}`

- Genereer een hexdump van een binair bestand en sla het op als een tekstbestand:

`xxd {{invoerbestand}} {{uitvoerbestand}}`

- Toon een compactere uitvoer, waarbij opeenvolgende nullen (indien aanwezig) vervangen worden door een sterretje:

`xxd {{[-a|-autoskip]}} {{invoerbestand}}`

- Toon de uitvoer met 10 kolommen van elk één octet (byte):

`xxd {{[-c|-cols]}} {{10}} {{invoerbestand}}`

- Toon alleen uitvoer tot een lengte van 32 bytes:

`xxd {{[-l|-len]}} {{32}} {{invoerbestand}}`

- Toon de uitvoer in platte modus, zonder ruimtes tussen de kolommen:

`xxd {{[-p|-postscript]}} {{invoerbestand}}`

- Zet een platte-tekst hexdump terug om naar binair en sla het op als een binair bestand:

`xxd {{[-r|-revert]}} {{[-p|-postscript]}} {{invoerbestand}} {{uitvoerbestand}}`
