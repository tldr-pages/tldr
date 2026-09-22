# kiterunner kb

> Een contextuele webscanner voor het manipuleren van kitebuilder-schema's die gebruikt worden in API en web endpoint discovery.
> Het `kb` subcommando zorgt voor schema compilatie, conversie, parsing en request replay.
> Meer informatie: <https://github.com/assetnote/kiterunner#usage>.

- Compileer een kitebuilder schema van JSON naar een kite bestand:

`kiterunner kb compile {{pad/naar/woordenlijst.json}} {{pad/naar/woordenlijst.kite}}`

- Converteer een kite bestand naar een tekst woordenlijst:

`kiterunner kb convert {{pad/naar/woordenlijst.kite}} {{pad/naar/woordenlijst.txt}}`

- Converteer een tekst woordenlijst naar een kite bestand:

`kiterunner kb convert {{pad/naar/woordenlijst.txt}} {{pad/naar/woordenlijst.kite}}`

- Converteer een kite bestand naar een JSON schema:

`kiterunner kb convert {{pad/naar/woordenlijst.kite}} {{pad/naar/woordenlijst.json}}`

- Parseer een kitebuilder schema en voer opgemaakte JSON data uit:

`kiterunner kb parse {{pad/naar/woordenlijst.json}} {{[-o|--output]}} {{json}}`

- Parseer een kite bestand en voer opgemaakte tekstgegevens uit:

`kiterunner kb parse {{pad/naar/woordenlijst.kite}} {{[-o|--output]}} {{text}}`

- Speel een specifiek verzoek van een kitebuilder schema-uitvoer opnieuw af:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{pad/naar/woordenlijst.kite}} "{{request_output}}"`

- Herhaal een verzoek via een proxy voor inspectie:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{pad/naar/woordenlijst.kite}} {{[-p|--proxy]}} {{http://localhost:8080}} "{{request_output}}"`
