# clang++

> Compileert C++ bronbestanden.
> Onderdeel van of LLVM.
> Meer informatie: <https://clang.llvm.org>.

- Compileer een broncodebestand naar een uitvoerbaar binair bestand:

`clang++ {{pad/naar/bron.cpp}} -o {{pad/naar/uitvoerbaar_bestand}}`

- Toon (bijna) alle fouten en waarschuwingen:

`clang++ {{pad/naar/bron.cpp}} -Wall -o {{pad/naar/uitvoerbaar_bestand}}`

- Kies een taalstandaard om mee te compileren:

`clang++ {{pad/naar/bron.cpp}} -std={{c++20}} -o {{pad/naar/uitvoerbaar_bestand}}`

- Voeg bibliotheken toe die zich op een ander pad bevinden dan het bronbestand:

`clang++ {{pad/naar/bron.cpp}} -o {{pad/naar/uitvoerbaar_bestand}} -I{{pad/naar/header_pad}} -L{{pad/naar/bibliotheek_pad}} -l{{pad/naar/bibliotheek_naam}}`

- Compileer broncode naar LLVM Intermediate Representation (IR):

`clang++ -S -emit-llvm {{pad/naar/bron.cpp}} -o {{pad/naar/uitvoer.ll}}`

- Optimaliseer het gecompileerde programma voor prestaties:

`clang++ {{pad/naar/bron.cpp}} -O{{1|2|3|fast}} -o {{pad/naar/uitvoerbaar_bestand}}`
