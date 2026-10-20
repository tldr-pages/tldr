# redshift

> Pas de kleurtemperatuur van een scherm aan op basis van de omgeving.
> Opmerking: Redshift ondersteunt geen Wayland.
> Zie ook: `gammastep`.
> Meer informatie: <https://manned.org/redshift>.

- Schakel Redshift in met een [t]emperatuur van 5700k overdag en 3600k 's nachts:

`redshift -t 5700:3600`

- Schakel Redshift in met een handmatig opgegeven [l]ocatie:

`redshift -l {{breedtegraad}}:{{lengtegraad}}`

- Schakel Redshift in met schermhelderheid ([b]rightness) ingesteld op 70% overdag en 40% 's nachts:

`redshift -b 0.7:0.4`

- Schakel Redshift in met aangepaste [g]amma-niveaus (tussen 0 en 1):

`redshift -g {{rood}}:{{groen}}:{{blauw}}`

- Verwijder ([P]) bestaande temperatuurveranderingen en stel een constante, onveranderlijke kleurtemperatuur in [O]ne-shot-modus in:

`redshift -PO {{temperatuur}}`
