# clang++

> Kompiliert C++ Quelldateien.
> Teil von LLVM.
> Weitere Informationen: <https://clang.llvm.org/docs/UsersManual.html#command-line-options>.

- Kompiliere eine Quelldatei in eine ausführbare Binärdatei:

`clang++ {{pfad/zu/quelldatei.cpp}} {{[-o|--output]}} {{pfad/zu/binärdatei}}`

- Zeige geläufige Fehler und Warnungen an:

`clang++ {{pfad/zu/quelldatei.cpp}} -Wall {{[-o|--output]}} {{pfad/zu/binärdatei}}`

- Wähle einen Sprachstandard für die Kompilation aus:

`clang++ {{pfad/zu/quelldatei.cpp}} -std={{c++20}} {{[-o|--output]}} {{pfad/zu/binärdatei}}`

- Binde Bibliotheken, die sich an einem anderen Pfad als die Quelldatei befinden, ein:

`clang++ {{pfad/zu/qelldatei.cpp}} {{[-o|--output]}} {{pfad/zu/binärdatei}} -I{{pfad/zu/headerdatei}} -L{{pfad/zu/bibliothek}} -l{{bibliotheksname}}`

- Kompiliere eine Quelldatei zu LLVM Intermediate Representation (IR):

`clang++ {{[-S|--assemble]}} -emit-llvm {{pfad/zu/quelldatei.cpp}} {{[-o|--output]}} {{pfad/zu/ir_datei.ll}}`
