# iostat

> Geeft statistieken weer voor apparaten en partities.
> Meer informatie: <https://manned.org/iostat>.

- Toon een rapport van CPU- en schijfstatistieken sinds het opstarten van het systeem:

`iostat`

- Toon een rapport van CPU- en schijfstatistieken met eenheden omgezet naar megabytes:

`iostat -m`

- Toon CPU-statistieken:

`iostat {{[-c|--compact]}}`

- Toon schijfstatistieken met schijfnamen (inclusief LVM):

`iostat -N`

- Toon uitgebreide schijfstatistieken met schijfnamen voor apparaat "sda":

`iostat -xN {{sda}}`

- Toon incrementele rapporten van CPU- en schijfstatistieken elke 2 seconden:

`iostat {{2}}`
