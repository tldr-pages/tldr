# clang++

> Kompiliert C++ Quelldateien.
> Teil von LLVM.
> Weitere Informationen: <https://clang.llvm.org>.

- Kompiliere eine Quelldatei in eine ausführbare Binärdatei:

`clang++ {{pfad/zu/quelldatei.cpp}} -o {{pfad/zu/binärdatei}}`

- Zeige geläufige Fehler und Warnungen an:

`clang++ {{pfad/zu/quelldatei.cpp}} -Wall -o {{pfad/zu/binärdatei}}`

- Wähle einen Sprachstandard für die Kompilation aus:

`clang++ {{pfad/zu/quelldatei.cpp}} -std={{c++20}} -o {{pfad/zu/binärdatei}}`

- Binde Bibliotheken, die sich an einem anderen Pfad als die Quelldatei befinden, ein:

`clang++ {{pfad/zu/qelldatei.cpp}} -o {{pfad/zu/binärdatei}} -I{{pfad/zu/headerdatei}} -L{{pfad/zu/bibliothek}} -l{{bibliotheksname}}`

- Kompiliere eine Quelldatei zu LLVM Intermediate Representation (IR):

`clang++ -S -emit-llvm {{pfad/zu/quelldatei.cpp}} -o {{pfad/zu/ir_datei.ll}}`
