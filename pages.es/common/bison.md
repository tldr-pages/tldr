# bison

> Generador de analizadores GNU.
> Más información: <https://manned.org/bison>.

- Compila un archivo de definición en tono con  bison:

`bison {{ruta/a/archivo.y}}`

- Compila en modo debug, lo que hace que el analizador sintáctico resultante escriba información adicional en `stdout`:

`bison {{[-t|--debug]}} {{ruta/a/archivo.y}}`

- Especifique el nombre del archivo de salida:

`bison {{[-o|--output]}} {{ruta/a/salida.c}} {{ruta/a/archivo.y}}`

- Sea detallista al compilar:

`bison {{[-v|--verbose]}}``
