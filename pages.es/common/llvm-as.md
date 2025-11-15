# llvm-as

> Ir de Representación intermedia LLVM (`.ll`) a Bitcode de Ensamblador (`.bc`).
> Más información: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

- Ensambla un archivo IR:

`llvm-as -o {{ruta/a/ensamblado.bc}} {{ruta/a/fuente.ll}}`

- Ensambla un archivo IR e incluye un hash de módulo en el archivo bitcode producido:

`llvm-as --module-hash -o {{ruta/a/ensamblado.bc}} {{ruta/a/fuente.ll}}`

- Lee un archivo IR de `stdin` y lo ensambla:

`cat {{ruta/a/fuente.ll}} | llvm-as -o {{ruta/a/ensamblado.bc}}`
