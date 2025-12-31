# libtoolize

> Een `autotools` tool om een pakket voor te bereiden voor het gebruik van `libtool`.
> Het voert verschillende taken uit, waaronder het genereren van de benodigde bestanden en directories om `libtool` naadloos in een project te integreren.
> Meer informatie: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- Initialiseer een project voor `libtool` door de benodigde bestanden te kopiëren (symbolische links vermijden) en bestaande bestanden indien nodig te overschrijven:

`libtoolize {{[-cf|--copy --force]}}`
