# xml2man

> Compila MPGL a mdoc.
> Más información: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

- Compila un archivo MPGL a una página man visible:

`xml2man {{ruta/al/archivo_de_comando.mxml}}`

- Compila un archivo MPGL a un archivo de salida específico:

`xml2man {{ruta/al/archivo_servicio.mxml}} {{ruta/al/archivo_servicio.7}}`

- Compila un archivo MPGL a un archivo de salida específico, sobrescribiéndolo si ya existe:

`xml2man -f {{ruta/al/archivo_funcion.mxml}} {{ruta/al/archivo_de_funcion.3}}`
