# nano

> Command-line tekst bewerker. Een verbeterde `Pico` kloon.
> Meer informatie: <https://nano-editor.org>.

- Start de tekst bewerker:

`nano`

- Start de tekst bewerker zonder gebruik te maken van configuratiebestanden:

`nano --ignorercfiles`

- Open specifieke bestanden, ga naar het volgende bestand bij het sluiten van de vorige:

`nano {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Open een bestand en positioneer de cursor op een specifieke regel en kolom:

`nano +{{regel}},{{kolom}} {{pad/naar/bestand}}`

- Open een bestand en zet 'soft wrapping' aan:

`nano --softwrap {{pad/naar/bestand}}`

- Open een bestand en spring nieuwe regels in volgens de inspringing van de vorige regel:

`nano --autoindent {{pad/naar/bestand}}`

- Open een bestand en maak een reservekopie (`pad/naar/bestand~`) bij het opslaan:

`nano --backup {{pad/naar/bestand}}`
