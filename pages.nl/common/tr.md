# tr

> Vertaal tekens: voer vervangingen uit op basis van enkele tekens en tekensets.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Vervang alle voorkomens van een teken in een bestand en toon het resultaat:

`tr < {{pad/naar/bestand}} {{vind_karakter}} {{vervang_karakter}}`

- Vervang alle voorkomens van een teken uit de uitvoer van een ander commando:

`echo {{tekst}} | tr {{vind_karakter}} {{vervang_karakter}}`

- Map elk teken van de eerste set naar het overeenkomstige teken van de tweede set:

`tr < {{pad/naar/bestand}} '{{abcd}}' '{{jkmn}}'`

- Verwijder alle voorkomens van de opgegeven set tekens uit de invoer:

`tr < {{pad/naar/bestand}} {{[-d|--delete]}} '{{invoer_karakters}}'`

- Comprimeer een reeks identieke tekens tot een enkel teken:

`tr < {{pad/naar/bestand}} {{[-s|--squeeze-repeats]}} '{{invoer_karakters}}'`

- Vertaal de inhoud van een bestand naar hoofdletters:

`tr < {{pad/naar/bestand}} "[:lower:]" "[:upper:]"`

- Verwijder niet-afdrukbare tekens uit een bestand:

`tr < {{pad/naar/bestand}} {{[-cd|--complement --delete]}} "[:print:]"`
