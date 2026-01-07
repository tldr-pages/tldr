# btm

> Muestra información del sistema sobre la CPU, la memoria, los discos, la red y los procesos.
> Una alternativa mejorada a `top`.
> Vea también: `btop`, `glances`, `atop`, `htop`, `top`.
> Más información: <https://clementtsang.github.io/bottom/nightly/#usage-and-configuration>.

- Muestra el diseño predeterminado (CPU, memoria, temperaturas, disco, red y procesos):

`btm`

- Habilita el modo básico, eliminando gráficos y condensando datos (similar a `top`):

`btm {{[-b|--basic]}}`

- Utiliza puntos grandes en lugar de pequeños en los gráficos:

`btm {{[-m|--dot_marker]}}`

- Muestra también la carga de la batería y el estado de salud:

`btm --battery`

- Actualiza cada 250 milisegundos y muestra los últimos 30 segundos en los gráficos:

`btm {{[-r|--rate]}} 250 {{[-t|--default_time_value]}} 30000`
