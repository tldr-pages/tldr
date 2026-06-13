# clang

> Compileer C, C++, en Objective-C bronbestanden. Kan gebruikt worden als een vervanger van GCC.
> Onderdeel van LLVM.
> Meer informatie: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compileer broncodebestand(en) naar een uitvoerbaar binair bestand:

`clang {{pad/naar/bron1.c pad/naar/bron2.c ...}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon (bijna) alle fouten en waarschuwingen:

`clang {{pad/naar/bron.c}} -Wall {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon veelvoorkomende waarschuwingen, debug-symbolen in de uitvoer, en optimaliseer zonder debugging te beïnvloeden:

`clang {{pad/naar/bron.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Voeg bibliotheken toe die zich op een ander pad bevinden dan het bronbestand:

`clang {{pad/naar/bron.c}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}} -I{{pad/naar/header}} -L{{pad/naar/bibliotheek}} -l{{bibliotheek_naam}}`

- Compileer broncode naar LLVM Intermediate Representation (IR):

`clang {{[-S|--assemble]}} -emit-llvm {{pad/naar/bron.c}} {{[-o|--output]}} {{pad/naar/uitvoer.ll}}`

- Compileer broncode zonder deze te linken:

`clang {{[-c|--compile]}} {{pad/naar/bron.c}}`

- Optimaliseer het gecompileerde programma voor prestaties:

`clang {{pad/naar/bron.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon de versie:

`clang --version`
