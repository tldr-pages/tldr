# clang

> Compila archivos fuente C, C+ y Objective-C. Se puede utilizar como un reemplazo para GCC.
> Parte de LLVM.
> Más información: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compila archivos de múltiples fuentes en un ejecutable:

`clang {{ruta/a/fuente1.c ruta/a/fuente2.c ...}} {{[-o|--output]}} {{ruta/al/ejecutable_resultante}}`

- Activa la salida de todos los errores y advertencias:

`clang {{ruta/a/fuente.c}} -Wall {{[-o|--output]}} {{ejecutable_resultante}}`

- Muestra advertencias comunes, depura símbolos en la salida y optimiza sin afectar la depuración:

`clang {{ruta/a/fuente.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{ruta/al/ejecutable_resultante}}`

- Incluye bibliotecas de una ruta diferente:

`clang {{ruta/a/fuente.c}} {{[-o|--output]}} {{ruta/al/ejecutable_resultante}} -I{{ruta/al/encabezado}} -L{{ruta/a/la/biblioteca}} -l{{nombre_biblioteca}}`

- Compila código fuente hacia representación intermedia (IR) LLVM:

`clang {{[-S|--assemble]}} -emit-llvm {{ruta/a/fuente.c}} {{[-o|--output]}} {{ruta/a/la/salida.ll}}`

- Compila código fuente en un archivo objeto sin vincular (linking):

`clang {{[-c|--compile]}} {{ruta/a/fuente.c}}`

- Optimiza el programa compilado para velocidad de ejecución:

`clang {{ruta/a/fuente.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{ruta/al/ejecutable_resultante}}`

- Muestra la versión:

`clang --version`
