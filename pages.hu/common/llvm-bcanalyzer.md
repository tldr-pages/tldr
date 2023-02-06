# llvm-bcanalyzer

> LLVM Bitcode (`.bc`) analizátor. További információ: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Statisztikák nyomtatása egy Bitcode fájlról:

`llvm-bcanalyzer {{path/to/file.bc}}`

- SGML-reprezentáció és statisztikák nyomtatása egy Bitcode fájlról:

`llvm-bcanalyzer -dump {{path/to/file.bc}}`

- Bitcode fájl beolvasása a `stdin` oldalról és elemzése:

`cat {{path/to/file.bc}} | llvm-bcanalyzer`
