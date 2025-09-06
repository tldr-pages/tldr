# dysk

> Muestra información del sistema de archivos en una tabla.
> Más información: <https://manned.org/dysk>.

- Obtén una visión general estándar de tus discos habituales:

`dysk`

- Ordena por tamaño libre:

`dysk {{[-s|--sort]}} free`

- Incluye solo discos HDD:

`dysk {{[-f|--filter]}} 'disk = HDD'`

- Excluye discos SSD:

`dysk {{[-f|--filter]}} 'disk <> SSD'`

- Muestra discos con alta ocupación o poco espacio libre:

`dysk {{[-f|--filter]}} 'use > 65% | free < 50G'`
