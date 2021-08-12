# clang

> Compilator pentru fișierele sursă C, C++ și Objective-C. Poate fi folosit ca înlocuitor drop-in pentru GCC.
> Mai multe informaţii: <https://clang.llvm.org/docs/ClangCommandLineReference.html>

- Compilarea unui fișier de cod sursă într-un binar executabil:

`clang {{input_source.c}} -o {{output_executable}}`

- Activați ieșirea tuturor erorilor și avertismentelor:

`clang {{input_source.c}} -Wall -o {{output_executable}}`

- Includeți bibliotecile situate la o altă cale decât fișierul sursă:

`clang {{input_source.c}} -o {{output_executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`

- Compilarea codului sursă în reprezentarea intermediară a LLVM (IR):

`clang -S -emit-llvm {{file.c}} -o {{file.ll}}`
