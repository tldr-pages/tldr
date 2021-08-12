# clang-format

> Instrument pentru a auto-formata C/C++/Javascript/Objective-C/Protobuf/C# cod.
> Mai multe informaţii: <https://clang.llvm.org/docs/ClangFormat.html>

- Formatați un fișier și imprimați rezultatul la stdout:

`clang-format {{path/to/file}}`

- Formatarea unui fișier în loc:

`clang-format -i {{path/to/file}}`

- Formatarea unui fișier utilizând un stil de codificare predefinit:

`clang-format --style={{LLVM|Google|Chromium|Mozilla|WebKit}} {{path/to/file}}`

- Formatarea unui fișier utilizând fișierul `.clang-format` într-unul din directoarele părinte ale fișierului sursă:

`clang-format --style=file {{path/to/file}}`

- Generează un fișier personalizat `.clang-format`:

`clang-format --style={{LLVM|Google|Chromium|Mozilla|WebKit}} --dump-config > {{.clang-format}}`
