# lex

> Generador de analizadores léxicos.
> Dada la especificación de un analizador léxico, genera código C implementándolo.
> Más información: <https://keith.github.io/xcode-man-pages/lex.1.html>.

- Genera un analizador a partir de un fichero Lex:

`lex {{analyzer.l}}`

- Especifica el fichero de salida:

`lex {{analyzer.l}} --outfile {{analyzer.c}}`

- Compila un archivo C generado por Lex:

`cc {{ruta/hacia/lex.yy.c}} --output {{ejecutable}}`
