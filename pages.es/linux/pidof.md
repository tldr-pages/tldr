# pidof

> Obtiene el ID de un proceso a partir de su nombre.
> Vea también: `pgrep`.
> Más información: <https://manned.org/pidof>.

- Muestra todos los ID de proceso con el nombre indicado:

`pidof {{bash}}`

- Muestra un único ID de proceso con el nombre indicado:

`pidof -s {{bash}}`

- Muestra los ID de los procesos, incluidos los scripts, con el nombre indicado:

`pidof -x {{script.py}}`

- Termina todos los procesos con el nombre indicado:

`kill $(pidof {{nombre}})`
