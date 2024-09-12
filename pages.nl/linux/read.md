# read

> Shell builtin voor het ophalen van data van `stdin`.
> Meer informatie: <https://manned.org/read.1p>.

- Sla gegevens op die je van het toetsenbord typt:

`read {{variable}}`

- Sla elke volgende regel die je invoert op als waarden van een array:

`read -a {{array}}`

- Specificeer het maximale aantal karakters dat gelezen moet worden:

`read -n {{character_count}} {{variable}}`

- Gebruik een specifiek teken als scheidingsteken in plaats van een nieuwe regel:

`read -d {{new_delimiter}} {{variable}}`

- Laat backslash (\\) niet optreden als een escape-teken:

`read -r {{variable}}`

- Toon een prompt vóór de invoer:

`read -p "{{Voer je invoer hier in: }}" {{variable}}`

- Echo de ingetikte tekens niet (stille modus):

`read -s {{variable}}`

- Lees `stdin` en voer een actie uit op elke regel:

`while read line; do echo "$line"; done`
