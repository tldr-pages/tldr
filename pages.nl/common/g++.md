# g++

> Compileer C++-bronbestanden.
> Onderdeel van GCC (GNU Compiler Collection).
> Meer informatie: <https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html>.

- Compileer een bronbestand in een uitvoerbaar bestand:

`g++ {{pad/naar/bron1.cpp pad/naar/bron2.cpp ...}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon alle fouten en waarschuwingen:

`g++ {{pad/naar/bron.cpp}} -Wall {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon veelvoorkomende waarschuwingen, debug-symbolen in de uitvoer, en optimaliseer zonder debugging te beïnvloeden:

`g++ {{pad/naar/bron.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Kies een taalstandaard om mee te compileren (C++98/C++11/C++14/C++17):

`g++ {{pad/naar/bron.cpp}} -std={{c++98|c++11|c++14|c++17}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Voeg bibliotheken toe die zich op een ander pad bevinden dan het bronbestand:

`g++ {{pad/naar/bron.cpp}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}} -I{{pad/naar/header}} -L{{pad/naar/bibliotheek}} -l{{bibliotheek_naam}}`

- Compileer en link meerdere bronbestanden tot één uitvoerbaar bestand:

`g++ {{[-c|--compile]}} {{pad/naar/bron1.cpp pad/naar/bron2.cpp ...}} && g++ {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}} {{pad/naar/bron1.o pad/naar/bron2.o ...}}`

- Optimaliseer het gecompileerde programma voor prestaties:

`g++ {{pad/naar/bron.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{pad/naar/uitvoerbaar_bestand}}`

- Toon de versie:

`g++ --version`
