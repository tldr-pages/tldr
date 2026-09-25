# gawk

> GNU-versie van awk, een veelzijdige programmeertaal voor het werken met bestanden.
> Zie ook: `awk`.
> Meer informatie: <https://www.gnu.org/software/gawk/manual/gawk.html>.

- Toon de vijfde kolom (a.k.a. veld) in een spatie-gescheiden bestand:

`gawk '{print $5}' {{pad/naar/bestand}}`

- Toon de tweede kolom van de regels die "foo" bevatten in een spatie-gescheiden bestand:

`gawk '/{{foo}}/ {print $2}' {{pad/naar/bestand}}`

- Toon de laatste kolom van elke regel in een bestand, met een komma (in plaats van spatie) als veldscheidingsteken:

`gawk {{[-F|--field-separator]}} ',' '{print $NF}' {{pad/naar/bestand}}`

- Tel de waarden in de eerste kolom van een bestand op en toon het totaal:

`gawk '{s+=$1} END {print s}' {{pad/naar/bestand}}`

- Toon elke derde regel, beginnend bij de eerste regel:

`gawk 'NR%3==1' {{pad/naar/bestand}}`

- Toon verschillende waarden op basis van voorwaarden:

`gawk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{pad/naar/bestand}}`

- Toon alle regels waarvan de waarde in de 10e kolom tussen een min en max ligt:

`gawk '($10 >= {{min_waarde}} && $10 <= {{max_waarde}})' {{pad/naar/bestand}}`

- Toon een tabel van gebruikers met UID >=1000 met koptekst en opgemaakte uitvoer, met een dubbele punt als scheidingsteken (`%-20s` betekent: 20 links uitgelijnde tekens, `%6s` betekent: 6 rechts uitgelijnde tekens):

`gawk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
