# read

> Shell builtin voor het ophalen van data van `stdin`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-read>.

- Sla gegevens op die je van het toetsenbord typt in een of meerdere variabelen:

`read {{variabele1 variabele2 ...}}`

- Sla elk van de volgende regels die je invoert op als waarden van een array:

`read -a {{array}}`

- Specificeer het maximale aantal karakters dat gelezen moet worden:

`read -n {{aantal_karakters}} {{variabele}}`

- Wijs meerdere waarden toe aan meerdere variabelen:

`read <<< "{{De achternaam is Bond}}" {{_ variabele1 _ variabele2}}`

- Laat backslash (`\`) niet optreden als een escape-teken:

`read -r {{variabele}}`

- Toon een prompt vóór de invoer:

`read -p "{{Voer je invoer hier in: }}" {{variabele}}`

- Echo de ingetikte tekens niet (stille modus):

`read -s {{variabele}}`

- Voer een actie uit op elke regel van de uitvoer van een commando:

`{{commando}} | while IFS= read -r line; do {{echo|ls|rm|...}} "$line"; done`
