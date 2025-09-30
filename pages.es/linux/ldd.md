# ldd

> Muestra dependencias de bibliotecas compartidas de un binario.
> No use en un binario no confiable, use `objdump` para esto en su lugar.
> Más información: <https://manned.org/ldd>.

- Muestra dependencias de biblioteca compartidas de un binario:

`ldd {{ruta/al/binario}}`

- Muestra toda la información sobre las dependencias:

`ldd --verbose {{ruta/al/binario}}`

- Muestra dependencias directas no utilizadas:

`ldd --unused {{ruta/al/binario}}`

- Reporta objetos de datos perdidos y realiza reubicaciones de datos:

`ldd --data-relocs {{ruta/al/binario}}`

- Reporta objetos y funciones de datos ausentes y los reubica a ambos:

`ldd --function-relocs {{ruta/al/binario}}`
