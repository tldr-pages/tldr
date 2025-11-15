# mpicc

> Open MPI C wrapper compiler.
> Meer informatie: <https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

- Compileer een bronbestand naar een objectbestand:

`mpicc -c {{pad/naar/bestand.c}}`

- Koppel een objectbestand en maak een executable:

`mpicc -o {{executable}} {{pad/naar/objectbestand.o}}`

- Compileer en koppel een bronbestand in één commando:

`mpicc -o {{executable}} {{pad/naar/bestand.c}}`
