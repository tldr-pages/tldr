# clang

> Compilatore per sorgenti C, C++ ed Objective-C. Può essere usato come alternativa a GCC.
> Maggiori informazioni: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compila un file sorgente in un binario eseguibile:

`clang {{sorgente_input.c}} {{[-o|--output]}} {{eseguibile_output}}`

- Attiva l'output di tutti gli errori ed i warning:

`clang {{sorgente_input.c}} -Wall {{[-o|--output]}} {{eseguibile_output}}`

- Includi librerie contenute in un percorso differente da quello del file di sorgente:

`clang {{sorgente_input.c}} {{[-o|--output]}} {{eseguibile_output}} -I{{percorso_header}} -L{{percorso_librerie}} -l{{nome_libreria}}`

- Compila codice sorgente in IR LLVM (Intermediate Representation):

`clang {{[-S|--assemble]}} -emit-llvm {{file.c}} {{[-o|--output]}} {{file.ll}}`
