# fold

> Breek elke regel in een invoerbestand af om in een gespecificeerde breedte te passen en toon het in `stdout`.
> Meer informatie: <https://manned.org/fold.1p>.

- Breek elke regel af op de standaard breedte (80 tekens):

`fold {{pad/naar/bestand}}`

- Breek elke regel af op een breedte van "30":

`fold -w30 {{pad/naar/bestand}}`

- Breek elke regel af op een breedte van "5" en breek de regel bij spaties (zet elk door spaties gescheiden woord op een nieuwe regel, woorden langer dan 5 tekens worden afgebroken):

`fold -w5 -s {{pad/naar/bestand}}`
