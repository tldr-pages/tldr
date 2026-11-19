# clang-format

> Programm zum Auto-Formatieren von C/C++/Java/JavaScript/Objective-C/Protobuf/C#-Code.
> Weitere Informationen: <https://clang.llvm.org/docs/ClangFormat.html>.

- Formatiere eine Datei und schreibe das Ergebnis nach `stdout`:

`clang-format {{pfad/zu/datei}}`

- Überschreibe eine Datei mit ihrem formatierten Inhalt:

`clang-format -i {{pfad/zu/datei}}`

- Formatiere eine Datei mit einem bestimmten Code-Stil:

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} {{pfad/zu/datei}}`

- Formatiere eine Datei mit der `.clang-format`-Datei aus einem der Überverzeichnisse der Quelldatei:

`clang-format --style file {{pfad/zu/datei}}`

- Generiere eine eigene `.clang-format`-Datei:

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} --dump-config >{{.clang-format}}`
