# gcc

> Preprocess en compileer C en C++ bronbestanden, monteer en koppel ze vervolgens samen.
> Meer informatie: <https://gcc.gnu.org>.

- Meerdere bronbestanden compileren in een uitvoerbaar bestand:

`gcc {{pad/naar/source1.c pad/naar/source2.c ...}} -o {{pad/naar/output_executable}}`

- Toon gemeenschappelijke waarschuwingen, foutopsporingssymbolen in output en optimaliseer zonder debuggen te beïnvloeden:

`gcc {{pad/naar/bron.c}} -Wall -g -Og -o {{pad/naar/output_executable}}`

- Neem bibliotheken op vanuit een ander pad:

`gcc {{pad/naar/bron.c}} -o {{pad/naar/output_executable}} -I{{pad/naar/header}} -L{{pad/naar/library}} -l{{library_name}}`

- Compileer broncode naar Assembler instructies:

`gcc -S {{pad/naar/bron.c}}`

- Compileer broncode naar een objectbestand zonder te koppelen:

`gcc -c {{pad/naar/bron.c}}`
