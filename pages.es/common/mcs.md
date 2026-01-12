# mcs

> Compilador Mono para C#.
> Más información: <https://manned.org/mcs>.

- Compila los archivos indicados:

`mcs {{ruta/al/archivo_entrada1.cs ruta/al/archivo_entrada2.cs ...}}`

- Indica el nombre del programa de salida:

`mcs -out:{{ruta/al/archivo.exe}} {{ruta/al/archivo_entrada1.cs ruta/al/archivo_entrada2.cs ...}}`

- Indica el tipo de programa de salida:

`mcs -target:{{exe|winexe|library|module}} {{ruta/al/archivo_entrada1.cs ruta/al/archivo_entrada2.cs ...}}`
