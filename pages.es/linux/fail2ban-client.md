# fail2ban-client

> Configura y controla un servidor Fail2Ban.
> Más información: <https://manned.org/fail2ban-client>.

- Consulta el estado del servicio de una cárcel:

`fail2ban-client status {{cárcel}}`

- Elimina una IP de la lista de IPs bloqueadas:

`fail2ban-client set {{cárcel}} unbanip {{ip}}`

- Comprueba que el servidor Fail2Ban sigue activo:

`fail2ban-client ping`
