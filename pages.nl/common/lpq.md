# lpq

> Toon de status van de printerwachtrij.
> Meer informatie: <https://openprinting.github.io/cups/doc/man-lpq.html>.

- Toon de wachtende taken van de standaardbestemming:

`lpq`

- Toon de wachtende taken van alle printers die versleuteling afdwingen:

`lpq -a -E`

- Toon de wachtende taken in een lang formaat:

`lpq -l`

- Toon de wachtende taken van een specifieke printer of klasse:

`lpq -P {{bestemming}}/{{instantie}}`

- Toon de wachtende taken elke n seconden totdat de wachtrij leeg is:

`lpq +{{interval}}`
