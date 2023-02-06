# llvm-as

> LLVM Intermediate Representation (`.ll`) to Bitcode (`.bc`) assembler. További információ: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

- Egy IR fájl összerakása:

`llvm-as -o {{path/to/out.bc}} {{path/to/source.ll}}`

- Egy IR fájl összerakása és a modul hash beillesztése az előállított Bitcode fájlba:

`llvm-as --module-hash -o {{path/to/out.bc}} {{path/to/source.ll}}`

- IR-fájl beolvasása a `stdin` oldalról és összerakása:

`cat {{path/to/source.ll}} | llvm-as -o {{path/to/out.bc}}`
