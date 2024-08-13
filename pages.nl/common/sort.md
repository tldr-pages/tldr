# sort

> Sorteer regels van tekstbestanden.
> Meer informatie: <https://www.gnu.org/software/coreutils/sort>.

- Sorteer een bestand in oplopende volgorde:

`sort {{pad/naar/bestand}}`

- Sorteer een bestand in aflopende volgorde:

`sort --reverse {{pad/naar/bestand}}`

- Sorteer een bestand op een niet-hoofdlettergevoelige manier:

`sort --ignore-case {{pad/naar/bestand}}`

- Sorteer een bestand met numerieke in plaats van alfabetische volgorde:

`sort --numeric-sort {{pad/naar/bestand}}`

- Sorteer `/etc/passwd` numeriek op het 3e veld van elke regel, gebruik makend van ":" als veldscheidingsteken:

`sort --field-separator={{:}} --key={{3n}} {{/etc/passwd}}`

- Sorteer zoals hierboven, maar wanneer items in het 3e veld gelijk zijn, sorteer op het 4e veld met getallen en exponenten:

`sort -t {{:}} -k {{3,3n}} -k {{4,4g}} {{/etc/passwd}}`

- Sorteer een bestand waarbij alleen unieke regels worden behouden:

`sort --unique {{pad/naar/bestand}}`

- Sorteer een bestand en schrijf de uitvoer naar het opgegeven uitvoerbestand (kan worden gebruikt om een bestand in-place te sorteren):

`sort --output={{pad/naar/bestand}} {{pad/naar/bestand}}`
