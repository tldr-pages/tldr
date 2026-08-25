# jobs

> Comando integrado del intérprete de comandos para ver información sobre los procesos iniciados por el intérprete de comandos actual.
> Las opciones distintas a `-l` y `-p` son exclusivas de Bash.
> Vea también: `fg`, `bg`, `disown`, `%`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-jobs>.

- Vea los trabajos generados por el shell actual:

`jobs`

- Muestra una lista de trabajos y sus ID de proceso:

`jobs -l`

- Muestra información sobre los trabajos cuyo estado ha cambiado:

`jobs -n`

- Muestra solo los ID de proceso:

`jobs -p`

- Muestra los procesos en ejecución:

`jobs -r`

- Muestra los procesos detenidos:

`jobs -s`
