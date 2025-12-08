# sort

> Sorteer regels van tekstbestanden.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

- Sorteer een bestand in oplopende volgorde:

`sort {{pad/naar/bestand}}`

- Sorteer een bestand in aflopende volgorde:

`sort {{[-r|--reverse]}} {{pad/naar/bestand}}`

- Sorteer een bestand op een niet-hoofdlettergevoelige manier:

`sort {{-f|--ignore-case}} {{pad/naar/bestand}}`

- Sorteer een bestand met numerieke in plaats van alfabetische volgorde:

`sort {{[-n|--numeric-sort]}} {{pad/naar/bestand}}`

- Sorteer `/etc/passwd` numeriek op het 3e veld van elke regel, gebruik makend van ":" als veldscheidingsteken:

`sort {{[-t|--field-separator]}} : {{[-k|--key]}} 3n {{/etc/passwd}}`

- Sorteer zoals hierboven, maar wanneer items in het 3e veld gelijk zijn, sorteer op het 4e veld met getallen en exponenten:

`sort {{[-t|--field-separator]}} : {{[-k|--key]}} 3,3n {{[-k|--key]}} 4,4g /etc/passwd`

- Sorteer een bestand waarbij alleen unieke regels worden behouden:

`sort {{[-u|--unique]}} {{pad/naar/bestand}}`

- Sorteer een bestand en schrijf de uitvoer naar het opgegeven uitvoerbestand (kan worden gebruikt om een bestand in-place te sorteren):

`sort {{[-o|--output]}} {{pad/naar/bestand}} {{pad/naar/bestand}}`
