# libtool

> Een generiek script voor bibliotheekondersteuning dat de complexiteit van het gebruik van gedeelde bibliotheken verbergt achter een consistente, draagbare interface.
> Meer informatie: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- Compileer een bronbestand naar een `libtool`-object:

`libtool {{[c|compile]}} gcc {{[-c|--compile]}} {{pad/naar/bron.c}} {{[-o|--output]}} {{pad/naar/bron.lo}}`

- Maak een bibliotheek of een uitvoerbaar bestand:

`libtool {{[l|link]}} gcc {{[-o|--output]}} {{pad/naar/bibliotheek.lo}} {{pad/naar/bron.lo}}`

- Stel automatisch het bibliotheekpad in zodat een ander programma niet-geïnstalleerde door `libtool` gegenereerde programma's of bibliotheken kan gebruiken:

`libtool {{[e|execute]}} gdb {{pad/naar/programma}}`

- Installeer een gedeelde bibliotheek:

`libtool {{[i|install]}} cp {{pad/naar/bibliotheek.la}} {{pad/naar/installatiemap}}`

- Voltooi de installatie van `libtool`-bibliotheken op het systeem:

`libtool {{[f|finish]}} {{pad/naar/installatiemap}}`

- Verwijder geïnstalleerde bibliotheken of uitvoerbare bestanden:

`libtool {{[u|uninstall]}} {{pad/naar/geïnstalleerde_bibliotheek.la}}`

- Verwijder niet-geïnstalleerde bibliotheken of uitvoerbare bestanden:

`libtool {{[cl|clean]}} rm {{pad/naar/bron.lo}} {{pad/naar/bibliotheek.la}}`
