# mcs

> Compilador Mono para C#.
> Más información: <https://manned.org/mcs.1>.

- Compila los archivos indicados:

`mcs {{ruta/a/archivo_entrada1.cs ruta/a/archivo_entrada2.cs ...}}`

- Indica el nombre del programa de salida:

`mcs -out:{{ruta/a/archivo.exe}} {{ruta/a/archivo_entrada1.cs ruta/a/archivo_entrada2.cs ...}}`

- Indica el tipo de programa de salida:

`mcs -target:{{exe|winexe|library|module}} {{ruta/a/archivo_entrada1.cs ruta/a/archivo_entrada2.cs ...}}`
