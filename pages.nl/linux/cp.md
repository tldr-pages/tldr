# cp

> Kopieer bestanden en mappen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Kopieer een bestand naar een andere locatie:

`cp {{pad/naar/bronbestand.ext}} {{pad/naar/doel_bestand.ext}}`

- Kopieer een bestand naar een andere map, maar behoud de bestandsnaam:

`cp {{pad/naar/bronbestand.ext}} {{pad/naar/doel_map}}`

- Kopieer de inhoud van een map recursief naar een andere locatie (als de doelmap bestaat, dan wordt de map hierin gekopieerd):

`cp {{[-r|--recursive]}} {{pad/naar/bron_map}} {{pad/naar/doel_map}}`

- Kopieer een map recursief, in uitgebreide modus (laat de bestandsvoortgang zien):

`cp {{[-vr|--verbose --recursive]}} {{pad/naar/bron_map}} {{pad/naar/doel_map}}`

- Kopieer meerdere bestanden tegelijk naar een map:

`cp {{[-t|--target-directory]}} {{pad/naar/doel_map}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Kopieer tekst bestanden naar een andere locatie, in interactieve modus (vraagt de gebruiker voordat er iets overschreven wordt):

`cp {{[-i|--interactive]}} {{*.txt}} {{pad/naar/doel_map}}`

- Volg symbolische links voordat deze gekopieerd worden:

`cp {{[-L|--dereference]}} {{link}} {{pad/naar/doel_map}}`

- Gebruik het volledige pad van de bron bestanden, creëer missende tussenliggende mappen tijdens het kopieëren:

`cp --parents {{pad/naar/bronbestand}} {{pad/naar/doel_bestand}}`
