# yacc

> Genera un analizador sintáctico LALR (en C) con un archivo de especificación de gramática formal.
> Vea también: `bison`.
> Más información: <https://manned.org/yacc.1p>.

- Crea un fichero `y.tab.c` con el código del analizador en C y compila el fichero de gramática con todas las declaraciones constantes necesarias para los valores. El fichero `y.tab.h` con las declaraciones se crea exclusivamente con la opción `-d`:

`yacc -d {{ruta/al/archivo_de_gramática.y}}`

- Compila un fichero de gramática con la descripción del analizador sintáctico y un informe de conflictos generados por ambigüedades en la gramática:

`yacc -d {{ruta/al/archivo_de_gramática.y}} -v`

- Compila un archivo de gramática, y prefija los nombres de los archivos de salida con un prefijo personalizado en lugar de `y`:

`yacc -d {{ruta/al/archivo_de_gramática.y}} -v -b {{prefijo}}`
