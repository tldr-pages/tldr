# libtool

> Een generiek script voor bibliotheekondersteuning dat de complexiteit van het gebruik van gedeelde bibliotheken verbergt achter een consistente, draagbare interface.
> Meer informatie: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- Compileer een bronbestand naar een `libtool`-object:

`libtool --mode=compile gcc -c {{pad/naar/bron.c}} -o {{pad/naar/bron.lo}}`

- Maak een bibliotheek of een uitvoerbaar bestand:

`libtool --mode=link gcc -o {{pad/naar/bibliotheek.lo}} {{pad/naar/bron.lo}}`

- Stel automatisch het bibliotheekpad in zodat een ander programma niet-geïnstalleerde door `libtool` gegenereerde programma's of bibliotheken kan gebruiken:

`libtool --mode=execute gdb {{pad/naar/programma}}`

- Installeer een gedeelde bibliotheek:

`libtool --mode=install cp {{pad/naar/bibliotheek.la}} {{pad/naar/installatiemap}}`

- Voltooi de installatie van `libtool`-bibliotheken op het systeem:

`libtool --mode=finish {{pad/naar/installatiemap}}`

- Verwijder geïnstalleerde bibliotheken of uitvoerbare bestanden:

`libtool --mode=uninstall {{pad/naar/geïnstalleerde_bibliotheek.la}}`

- Verwijder niet-geïnstalleerde bibliotheken of uitvoerbare bestanden:

`libtool --mode=clean rm {{pad/naar/bron.lo}} {{pad/naar/bibliotheek.la}}`
