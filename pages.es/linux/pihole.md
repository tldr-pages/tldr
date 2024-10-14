# pihole

> Interfaz de terminal para el servidor DNS de bloqueo de anuncios Pi-hole.
> Más información: <https://docs.pi-hole.net/core/pihole-command/>.

- Verifica el estado del daemon de Pi-hole:

`pihole status`

- Actualiza Pi-hole y Gravity:

`pihole -up`

- Monitorea el estado detallado del sistema:

`pihole chronometer`

- Inicia o detiene el daemon:

`pihole {{enable|disable}}`

- Reinicia el daemon (no el servidor en sí):

`pihole restartdns`

- Incluye en lista blanca o negra un dominio:

`pihole {{whitelist|blacklist}} {{ejemplo.com}}`

- Busca en las listas un dominio:

`pihole query {{ejemplo.com}}`

- Abre un registro de conexiones en tiempo real:

`pihole tail`
