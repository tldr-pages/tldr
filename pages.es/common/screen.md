# screen

> Mantiene una sesión abierta en un servidor remoto. Gestiona varias ventanas con una única conexión SSH.
> Vea también: `tmux`, `zellij`.
> Más información: <https://manned.org/screen>.

- Inicia una nueva sesión de pantalla:

`screen`

- Inicia una nueva sesión de pantalla con nombre:

`screen -S {{nombre_de_sesión}}`

- Inicia un nuevo programa residente y registra la salida en `screenlog.x`:

`screen -dmLS {{nombre_de_sesión}} {{comando}}`

- Muestra las sesiones de pantalla abiertas:

`screen -ls`

- Vuelve a conectarse a una pantalla abierta:

`screen -r {{nombre_de_sesión}}`

- Se desvincula desde dentro de una pantalla:

`<Ctrl a><d>`

- Finaliza la sesión de pantalla actual:

`<Ctrl a><k>`

- Desactiva una pantalla desacoplada:

`screen -X -S {{nombre_de_sesión}} quit`
