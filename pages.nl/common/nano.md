# nano

> Simpele, makkelijk te gebruiken command-line tekst bewerker. Een verbeterde, gratis Pico kloon.
> Meer informatie: <https://nano-editor.org>.

- Open een nieuw bestand in nano:

`nano`

- Open een specifiek bestand:

`nano {{pad/naar/bestand}}`

- Open een bepaald bestand, met de cursor gezet in een gegeven regel en kolom:

`nano +{{regel}},{{kolom}} {{pad/naar/bestand}}`

- Open een bepaald bestand en zet 'soft wrapping' aan:

`nano --softwrap {{pad/naar/bestand}}`

- Open een bepaald bestand en spring nieuwe regels in volgens de inspringing van de vorige regel:

`nano --autoindent {{pad/naar/bestand}}`

- Open nano en maak een reservekopie (`bestand~`) bij het opslaan van veranderingen:

`nano --backup {{pad/naar/bestand}}`
