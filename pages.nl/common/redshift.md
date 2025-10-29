# redshift

> Pas de kleurtemperatuur van een scherm aan op basis van de omgeving.
> Note: Redshift does not support Wayland.
> Meer informatie: <https://manned.org/redshift>.

- Schakel Redshift in met een specifieke [t]emperatuur overdag (bijv. 5700K) en 's nachts (bijv. 3600K):

`redshift -t 5700:3600`

- Schakel Redshift in met een handmatig opgegeven [l]ocatie:

`redshift -l {{breedtegraad}}:{{lengtegraad}}`

- Schakel Redshift in met een specifieke schermhelderheid ([b]rightness) overdag (bijv. 70%) en 's nachts (bijv. 40%):

`redshift -b 0.7:0.4`

- Schakel Redshift in met aangepaste [g]amma-niveaus (tussen 0 en 1):

`redshift -g {{rood}}:{{groen}}:{{blauw}}`

- Verwijder ([P]urge) bestaande temperatuurveranderingen en stel een constante, onveranderlijke kleurtemperatuur in [O]ne-shot-modus in:

`redshift -PO {{temperatuur}}`
