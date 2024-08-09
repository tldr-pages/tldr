# dysk

> Muestra información del sistema de archivos en una tabla.
> Más información: <https://dystroy.org/dysk>.

- Obtén una visión general estándar de tus discos habituales:

`dysk`

- Ordena por tamaño libre:

`dysk --sort free`

- Incluye solo discos HDD:

`dysk --filter 'disk = HDD'`

- Excluye discos SSD:

`dysk --filter 'disk <> SSD'`

- Muestra discos con alta ocupación o poco espacio libre:

`dysk --filter 'use > 65% | free < 50G'`
