# llvm-bcanalyzer

> Analizador de bitcode LLVM (`.bc`).
> Más información: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Imprime estadísticas sobre un archivo bitcode:

`llvm-bcanalyzer {{ruta/al/archivo.bc}}`

- Imprime una representación SGML y estadísticas sobre un archivo bitcode:

`llvm-bcanalyzer -dump {{ruta/al/archivo.bc}}`

- Lee un archivo bitcode de `stdin` y lo analiza:

`cat {{ruta/al/archivo.bc}} | llvm-bcanalyzer`
