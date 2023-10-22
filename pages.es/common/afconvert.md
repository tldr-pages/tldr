# afconvert

> Convierte entre formatos de archivo AFF y raw.
> Más información: <https://manned.org/afconvert.1>.

- Utiliza una extensión específica (predeterminado: `aff`):

`afconvert -a {{extension}} {{ruta/al/archivo_de_entrada}} {{ruta/al/archivo_salida1 ruta/al/archivo_salida2 ...}}`

- Utiliza un nivel de compresión específico (predeterminado: `7`):

`afconvert -X{{0..7}} {{ruta/al/archivo_de_entrada}} {{ruta/al/archivo_salida1 ruta/al/archivo_salida2 ...}}`
