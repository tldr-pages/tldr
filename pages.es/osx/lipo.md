# lipo

> Herramienta para el manejo de binarios universales Mach-O.
> Más información: <https://ss64.com/osx/lipo.html>.

- Crea un archivo universal a partir de dos archivos de una sola arquitectura:

`lipo {{ruta/al/archivo/binario.x86_64}} {{ruta/al/archivo_binario.arm64e}} -create -output {{ruta/al/archivo_binario}}`

- Lista todas las arquitecturas contenidas en un archivo universal:

`lipo {{ruta/al/archivo_binario}} -archs`

- Muestra información detallada sobre un archivo universal:

`lipo {{ruta/al/archivo_binario}} -detailed_info`

- Extrae un archivo de arquitectura única de un archivo universal:

`lipo {{ruta/al/archivo_binario}} -thin {{arm64e}} -output {{ruta/al/archivo_binario.arm64e}}`
