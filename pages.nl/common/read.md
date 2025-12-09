# read

> Shell builtin voor het ophalen van data van `stdin`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-read>.

- Sla gegevens op die je van het toetsenbord typt:

`read {{variable}}`

- Sla elke van de volgende regels die je invoert op als waarden van een array:

`read -a {{array}}`

- Specificeer het maximale aantal karakters dat gelezen moet worden:

`read -n {{character_count}} {{variable}}`

- Wijs meerdere waarden toe aan meerdere variabelen:

`read <<< "{{De achternaam is Bond}}" {{_ variable1 _ variable2}}`

- Laat backslash (\\) niet optreden als een escape-teken:

`read -r {{variable}}`

- Toon een prompt vóór de invoer:

`read -p "{{Voer je invoer hier in: }}" {{variable}}`

- Echo de ingetikte tekens niet (stille modus):

`read -s {{variable}}`

- Lees `stdin` en voer een actie uit op elke regel:

`while read line; do {{echo|ls|rm|...}} "$line"; done < {{/dev/stdin|pad/naar/bestand|...}}`
