# flex

> Generador de analizadores léxicos.
> Dada la especificación de un analizador léxico, genera código C para su implementación.
> Más información: <https://manned.org/lex.1>.

- Genera un analizador a partir de un fichero Lex, almacenándolo en el archivo `lex.yy.c`:

`flex {{analyzer.l}}`

- Escribe el analizador en `stdout`:

`flex {{[-t|--stdout]}} {{analyzer.l}}`

- Especifica el archivo de salida:

`flex {{analyzer.l}} {{[-o|--outfile]}} {{analyzer.c}}`

- Genera un analizador por lotes en lugar de un analizador interactivo:

`flex {{[-B|--batch]}} {{analyzer.l}}`

- Compila un archivo C generado por Lex:

`cc {{ruta/a/lex.yy.c}} -o {{ejecutable}}`
