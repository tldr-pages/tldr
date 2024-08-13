# tr

> Vertaal tekens: voer vervangingen uit op basis van enkele tekens en tekensets.
> Meer informatie: <https://www.gnu.org/software/coreutils/tr>.

- Vervang alle voorkomens van een teken in een bestand en toon het resultaat:

`tr {{vind_karakter}} {{vervang_karakter}} < {{pad/naar/bestand}}`

- Vervang alle voorkomens van een teken uit de uitvoer van een ander commando:

`echo {{tekst}} | tr {{vind_karakter}} {{vervang_karakter}}`

- Map elk teken van de eerste set naar het overeenkomstige teken van de tweede set:

`tr '{{abcd}}' '{{jkmn}}' < {{pad/naar/bestand}}`

- Verwijder alle voorkomens van de opgegeven set tekens uit de invoer:

`tr -d '{{invoer_karakters}}' < {{pad/naar/bestand}}`

- Comprimeer een reeks identieke tekens tot een enkel teken:

`tr -s '{{invoer_karakters}}' < {{pad/naar/bestand}}`

- Vertaal de inhoud van een bestand naar hoofdletters:

`tr "[:lower:]" "[:upper:]" < {{pad/naar/bestand}}`

- Verwijder niet-afdrukbare tekens uit een bestand:

`tr -cd "[:print:]" < {{pad/naar/bestand}}`
