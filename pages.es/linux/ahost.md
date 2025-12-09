# ahost

> Herramienta de búsqueda DNS para mostrar el registro A o AAAA asociado con un nombre de host o dirección IP.
> Más información: <https://manned.org/ahost>.

- Muestra un registro `A` o `AAAA` asociado con un nombre de host o dirección IP:

`ahost {{example.com}}`

- Muestra salida adicional de depuración:

`ahost -d {{example.com}}`

- Muestra el registro con un tipo especificado:

`ahost -t {{a|aaaa|u}} {{example.com}}`
