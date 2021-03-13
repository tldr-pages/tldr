# gplusplus

> Kompiliere C++ Quelldateien.
> Teil der GCC (GNU Compiler Collection).
> Mehr  Informationen: <https://gcc.gnu.org>.

- Kompiliere eine Quelldatei in eine ausführbare Binärdatei:

`g++ {{quelldatei.cpp}} -o {{output_datei}`

- Zeige (fast) alle Fehler und Warnungen an:

`g++ {{quelldatei.cpp}} -Wall -o {{output_datei}}`

- Wähle einen Sprachstandard für das Kompilieren:

`g++ {{quelldatei.cpp}} -std={{C++98|C++11|C++14|C++17}} -o {{output_datei}}`

- Binde Bibliotheken, die sich an einem anderen Pfad als die Quelldatei befinden mit ein:

`g++ {{quelldatei.cpp}} -o {{output_datei}} -I{{header_pfad}} -L{{bibliotheks_pfad}} -l{{bibliotheks_name}}`
