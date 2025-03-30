# indent

> Wijzig het uiterlijk van een C/C++-programma door spaties in te voegen of te verwijderen.
> Meer informatie: <https://www.gnu.org/software/indent/manual/indent/Option-Summary.html>.

- Formatteer C/C++-broncode volgens de Linux style guide, maak automatisch een back-up van de originele bestanden en vervang deze door de ingesprongen versies:

`indent --linux-style {{pad/naar/bron.c}} {{pad/naar/andere_bron.c}}`

- Formatteer C/C++-broncode volgens de GNU-stijl en sla de ingesprongen versie op in een ander bestand:

`indent --gnu-style {{pad/naar/bron.c}} -o {{pad/naar/indented_source.c}}`

- Formatteer C/C++-broncode volgens de stijl van Kernighan & Ritchie (K&R), geen tabs, 3 spaties per inspringing en breek regels af op 120 tekens:

`indent --k-and-r-style --indent-level3 --no-tabs --line-length120 {{pad/naar/bron.c}} -o {{pad/naar/indented_source.c}}`
