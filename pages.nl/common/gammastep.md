# gammastep

> Pas de kleurtemperatuur van een scherm aan op basis van het tijdstip van de dag.
> Zie ook: `redshift`.
> Meer informatie: <https://manned.org/gammastep>.

- Schakel Gammastep in met een [t]emperatuur van 5700k overdag en 3600k 's nachts:

`gammastep -t 5700:3600`

- Schakel Gammastep in met een handmatig opgegeven aangepaste [l]ocatie:

`gammastep -l {{breedtegraad}}:{{lengtegraad}}`

- Schakel Gammastep in met schermhelderheid ([b]rightness) ingesteld op 70% overdag en 40% 's nachts:

`gammastep -b 0.7:0.4`

- Schakel Gammastep in met aangepaste [g]amma-niveaus (tussen 0 en 1):

`gammastep -g {{rood}}:{{groen}}:{{blauw}}`

- Schakel Gammastep in met een c[O]nstante, onveranderlijke kleurtemperatuur:

`gammastep -O {{temperatuur}}`

- Reset de temperatuuraanpassingen die door Gammastep zijn toegepast:

`gammastep -x`
