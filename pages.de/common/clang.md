# clang

> Compiler für C, C++ und Objective-C Quelldateien. Kann als Ersatz für GCC genutzt werden.
> Weitere Informationen: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Kompiliere eine Quelldatei in eine ausführbare Binärdatei:

`clang {{pfad/zu/quelldatei.c}} -o {{pfad/zu/binärdatei}}`

- Zeige geläufige Fehler und Warnungen an:

`clang {{pfad/zu/quelldatei.c}} -Wall -o {{pfad/zu/binärdatei}}`

- Binde Bibliotheken, die sich an einem anderen Pfad als die Quelldatei befinden, ein:

`clang {{pfad/zu/quelldatei.c}} -o {{pfad/zu/binärdatei}} -I{{pfad/zu/headerdatei}} -L{{pfad/zu/bibliothek}} -l{{bibliotheks_name}}`

- Kompiliere eine Quelldatei zu LLVM Intermediate Representation (IR):

`clang -S -emit-llvm {{pfad/zu/quelldatei.c}} -o {{pfad/zu/ir_datei.ll}}`

- Kompiliere eine Quelldatei, ohne zu Linken:

`clang -c {{pfad/zu/quelldatei.c}}`
