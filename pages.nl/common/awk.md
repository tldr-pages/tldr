# awk

> Een veelzijdige programmeertaal voor het werken met bestanden.
> Meer informatie: <https://github.com/onetrueawk/awk>.

- Toon de vijfde kolom (a.k.a. veld) in een spatie-gescheiden bestand:

`awk '{print $5}' {{pad/naar/bestand}}`

- Toon de tweede kolom van de regels die "foo" bevatten in een spatie-gescheiden bestand:

`awk '/{{foo}}/ {print $2}' {{pad/naar/bestand}}`

- Toon de laatste kolom van iedere regel in een bestand en maak gebruik van een komma (in plaats van een spatie) als veld scheider:

`awk -F ',' '{print $NF}' {{pad/naar/bestand}}`

- Tel de waarden in de eerste kolom van een bestand op en toon het totaal:

`awk '{s+=$1} END {print s}' {{pad/naar/bestand}}`

- Toon iedere derde regel startend vanaf de eerste regel:

`awk 'NR%3==1' {{pad/naar/bestand}}`

- Toon verschillende waardes gebaseerd op condities:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{pad/naar/bestand}}`

- Toon alle regels waarbij de waarde van de 10e kolom gelijk is aan de gespecificeerde waarde:

`awk '($10 == {{value}})'`

- Toon alle regels waarbij de waarde van de 10e kolom tussen een min en een max zit:

`awk '($10 >= {{min_value}} && $10 <= {{max_value}})'`
