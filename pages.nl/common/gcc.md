# gcc

> Preprocess en compileer C en C++ bronbestanden, monteer en koppel ze vervolgens samen.
> Onderdeel van GCC (GNU Compiler Collection).
> Meer informatie: <https://gcc.gnu.org/onlinedocs/gcc/>.

- Compileer meerdere bronbestanden in een uitvoerbaar bestand:

`gcc {{pad/naar/bron1.c pad/naar/bron2.c ...}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon (bijna) alle fouten en waarschuwingen:

`gcc {{pad/naar/bron.c}} -Wall {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon veelvoorkomende waarschuwingen, debug-symbolen in de uitvoer, en optimaliseer zonder debugging te beïnvloeden:

`gcc {{pad/naar/bron.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Voeg bibliotheken toe die zich op een ander pad bevinden dan het bronbestand:

`gcc {{pad/naar/bron.c}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}} -I{{pad/naar/header}} -L{{pad/naar/bibliotheek}} -l{{bibliotheek_naam}}`

- Compileer broncode naar Assembler instructies:

`gcc {{[-S|--assemble]}} {{pad/naar/bron.c}}`

- Compileer broncode zonder deze te linken:

`gcc {{[-c|--compile]}} {{pad/naar/bron.c}}`

- Optimaliseer het gecompileerde programma voor prestaties:

`gcc {{pad/naar/bron.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon de versie:

`gcc --version`
