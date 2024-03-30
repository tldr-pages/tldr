# clang

> Compiler voor C, C++, en Objective-C bronbestanden. Kan gebruikt worden als een vervanger van GCC.
> Meer informatie: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compileer een broncodebestand naar een uitvoerbaar binair bestand:

`clang {{invoer_bron.c}} -o {{uitvoerbaar_bestand}}`

- Toon alle fouten en waarschuwingen:

`clang {{invoer_bron.c}} -Wall -o {{uitvoerbaar_bestand}}`

- Voeg bibliotheken toe die zich op een ander pad bevinden dan het bronbestand:

`clang {{invoer_bron.c}} -o {{uitvoerbaarbestand}} -I{{header_pad}} -L{{bibliotheek_ad}} -l{{bibliotheek_naam}}`

- Compileer broncode naar LLVM Intermediate Representation (IR):

`clang -S -emit-llvm {{bestand.c}} -o {{bestand.ll}}`

- Compileer broncode zonder deze te linken:

`clang -c {{invoer_bron.c}}`

- Optimaliseer het gecompileerde programma voor prestaties:

`clang {{pad/naar/bron.c}} -O{{1|2|3|fast}}`
