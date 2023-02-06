# afconvert

> Convierte entre formatos de archivo AFF y raw.
> Más información: <https://manned.org/afconvert.1>.

- Utiliza una extensión específica (por defecto: `aff`):

`afconvert -a {{extension}} {{ruta/a/archivo_de_entrada}} {{ruta/a/archivo_salida1 ruta/a/archivo_salida2 ...}}`.

- Utiliza un nivel de compresión específico (por defecto: `7`):

`afconvert -X{{0..7}} {{ruta/a/archivo_de_entrada}} {{ruta/a/archivo_salida1 ruta/a/archivo_salida2 ...}}`.
