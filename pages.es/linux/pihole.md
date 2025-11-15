# pihole

> Interfaz de terminal para el servidor DNS de bloqueo de anuncios Pi-hole.
> Más información: <https://docs.pi-hole.net/main/pihole-command>.

- Verifica el estado del programa residente de Pi-hole:

`pihole status`

- Actualiza Pi-hole y Gravity:

`pihole {{[-up|updatePihole]}}`

- Inicia o detiene el programa residente:

`pihole {{enable|disable}}`

- Incluye en lista blanca o negra un dominio:

`pihole {{allowlist|denylist}} {{example.com}}`

- Busca en las listas un dominio:

`pihole {{[-q|query]}} {{example.com}}`

- Abre un registro de conexiones en tiempo real:

`pihole {{[-t|tail]}}`
