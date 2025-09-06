# strings

> Encuentra cadenas imprimibles en un archivo objeto o binario.
> Más información: <https://manned.org/strings>.

- Imprime todas las cadenas contenidas en un binario:

`strings {{ruta/al/archivo}}`

- Limita resultados a cadenas por lo menos n caracteres de largo:

`strings {{[-n|--bytes]}} {{n}} {{ruta/al/archivo}}`

- Precede cada resultado con su distancia hasta el inicio (offset) del archivo:

`strings {{[-t|--radix]}} d {{ruta/al/archivo}}`

- Precede cada resultado con su desplazamiento (offset) dentro del archivo en hexadecimal:

`strings {{[-t|--radix]}} x {{ruta/al/archivo}}`
