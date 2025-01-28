# addr2line

> Convierte direcciones de un binario en nombres de archivos y números de línea.
> Más información: <https://manned.org/addr2line>.

- Muestra el nombre de archivo y el número de línea del código fuente desde una dirección de instrucción de un ejecutable:

`addr2line --exe={{ruta/a/ejecutable}} {{dirección}}`

- Muestra el nombre de la función, nombre de archivo y número de línea:

`addr2line --exe={{ruta/a/ejecutable}} --functions {{dirección}}`

- Decodifica (demangle) el nombre de la función para código C++:

`addr2line --exe={{ruta/a/ejecutable}} --functions --demangle {{dirección}}`
