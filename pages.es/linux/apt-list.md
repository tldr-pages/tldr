# apt list

> Lista paquetes.
> Nota: Se recomienda ejecutar `apt update` primero para actualizar el índice local de paquetes.
> Más información: <https://manned.org/apt.8>.

- Lista todos los paquetes disponibles:

`apt list`

- Lista paquetes filtrando solo por nombre (admite comodines como `*`):

`apt list {{paquete}}`

- Lista los paquetes instalados:

`apt list {{[-i|--installed]}}`

- Lista los paquetes actualizables:

`apt list {{[-u|--upgradable]}}`
