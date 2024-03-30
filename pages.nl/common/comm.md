# comm

> Toon overeenkomstige regels tussen twee bestanden. Beide bestanden dienen gesorteerd te zijn.
> Meer informatie: <https://www.gnu.org/software/coreutils/comm>.

- Produceer drie tab-gescheiden kolommen: regels die alleen voorkomen in het eerste bestand, regels die alleen voorkomen in het tweede bestand en overeenkomstige regels tussen beide bestanden:

`comm {{bestand1}} {{bestand2}}`

- Toon alleen overeenkomstige regels van beide bestanden:

`comm -12 {{bestand1}} {{bestand2}}`

- Toon alleen de overeenkomstige regels van beide bestanden en lees een bestand vanaf `stdin`:

`cat {{bestand1}} | comm -12 - {{bestand2}}`

- Sla regels die alleen in het eerste bestand worden gevonden op in een derde bestand:

`comm -23 {{bestand1}} {{bestand2}} > {{alleen_bestand1}}`

- Toon de regels welke alleen in het tweede bestand gevonden worden, als de bestanden niet gesorteerd zijn:

`comm -13 <(sort {{bestand1}}) <(sort {{bestand2}})`
