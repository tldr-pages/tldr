# iwctl

> Controla el suplicante de red `iwd`.
> Vea también: `nmcli`, `iw`.
> Más información: <https://manned.org/iwctl>.

- Ejecuta `iwctl` en modo interactivo:

`iwctl`

- Muestra las estaciones Wi-Fi:

`iwctl station list`

- Busca redes con una estación:

`iwctl station {{estación}} scan`

- Muestra las redes encontradas por una estación:

`iwctl station {{estación}} get-networks`

- Conectarse a una red con una estación; si se necesitan credenciales, se solicitarán:

`iwctl station {{estación}} connect {{nombre_red}}`

- Muestra la ayuda:

`iwctl {{[-h|--help]}}`
