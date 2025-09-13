# nano

> Tekst bewerker. Een verbeterde `pico` kloon.
> Zie ook: `pico`, `rnano`.
> Meer informatie: <https://nano-editor.org/dist/latest/nano.html>.

- Open specifieke bestanden, ga naar het volgende bestand bij het sluiten van de vorige:

`nano {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Start de tekst bewerker zonder gebruik te maken van configuratiebestanden:

`nano {{[-I|--ignorercfiles]}}`

- Open een bestand en positioneer de cursor op een specifieke regel en kolom:

`nano +{{regel}},{{kolom}} {{pad/naar/bestand}}`

- Open een bestand en zet 'soft wrapping' aan:

`nano {{[-S|--softwrap]}} {{pad/naar/bestand}}`

- Open een bestand en spring nieuwe regels in volgens de inspringing van de vorige regel:

`nano {{[-i|--autoindent]}} {{pad/naar/bestand}}`

- Open een bestand en maak een reservekopie (`pad/naar/bestand~`) bij het opslaan:

`nano {{[-B|--backup]}} {{pad/naar/bestand}}`

- Open een bestand in de beperkte modus (d.w.z. lees/schrijf niet naar bestanden die niet op de command-line zijn gespecificeerd):

`nano {{[-R|--restricted]}} {{pad/naar/bestand}}`

- Sluit nano:

`<Ctrl x>`
