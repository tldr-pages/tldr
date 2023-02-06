# clang-format

> C/C++/Java/JavaScript/Objective-C/Protobuf/C# kód automatikus formázására szolgáló eszköz. További információ: <https://clang.llvm.org/docs/ClangFormat.html>.

- Egy fájl formázása és az eredmény kiírása a `stdout` címre:

`clang-format {{path/to/file}}`

- Egy fájl helyben történő formázása:

`clang-format -i {{path/to/file}}`

- Formázzon meg egy fájlt egy előre meghatározott kódolási stílus segítségével:

`clang-format --style={{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} {{path/to/file}}`

- Fájl formázása a forrásfájl egyik szülői könyvtárában található `.clang-format` fájl segítségével:

`clang-format --style=file {{path/to/file}}`

- Egyéni `.clang-format` fájl generálása:

`clang-format --style={{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} --dump-config > {{.clang-format}}`
