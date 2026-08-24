# clang

> Compila sorgenti C, C++ e Objective-C. Può essere usato come sostituto diretto di GCC.
> Parte di LLVM.
> Maggiori informazioni: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compila più file sorgente in un eseguibile:

`clang {{percorso/del/sorgente1.c percorso/del/sorgente2.c ...}} {{[-o|--output]}} {{percorso/dell/eseguibile_output}}`

- Attiva l'output di tutti gli errori e i warning:

`clang {{percorso/del/sorgente.c}} -Wall {{[-o|--output]}} {{eseguibile_output}}`

- Mostra i warning più comuni, i simboli di debug nell'output e ottimizza senza compromettere il debug:

`clang {{percorso/del/sorgente.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{percorso/dell/eseguibile_output}}`

- Includi librerie da un percorso diverso:

`clang {{percorso/del/sorgente.c}} {{[-o|--output]}} {{percorso/dell/eseguibile_output}} -I{{percorso/del/header}} -L{{percorso/della/libreria}} -l{{nome_libreria}}`

- Compila il codice sorgente in LLVM Intermediate Representation (IR):

`clang {{[-S|--assemble]}} -emit-llvm {{percorso/del/sorgente.c}} {{[-o|--output]}} {{percorso/dell/output.ll}}`

- Compila il codice sorgente in un file oggetto senza fare il linking:

`clang {{[-c|--compile]}} {{percorso/del/sorgente.c}}`

- Ottimizza il programma compilato per le prestazioni:

`clang {{percorso/del/sorgente.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{percorso/dell/eseguibile_output}}`

- Mostra la versione:

`clang --version`
