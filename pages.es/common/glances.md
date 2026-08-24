# glances

> Una herramienta multiplataforma para supervisar el sistema.
> Vea también: `htop`, `atop`, `top`, `btm`, `btop`.
> Más información: <https://nicolargo.github.io/glances/>.

- Se ejecuta en la terminal:

`glances`

- Se ejecuta en modo servidor web para mostrar los resultados en el navegador:

`glances {{[-w|--webserver]}}`

- Se ejecuta en modo servidor para permitir conexiones desde otros clientes Glances:

`glances {{[-s|--server]}}`

- Se conecta a un servidor Glances:

`glances {{[-c|--client]}} {{nombre_del_host}}`

- Solicita una contraseña en modo servidor (web):

`glances {{[-s|--server]}} --password`

- Sale de Glances:

`<q>`

- Muestra la ayuda:

`glances {{[-h|--help]}}`
