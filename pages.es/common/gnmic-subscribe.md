# gnmic subscribe

> Suscribirse a las actualizaciones de estado de un dispositivo de red gnmic.
> Más información: <https://gnmic.openconfig.net/cmd/subscribe/>.

- Suscribirse a las actualizaciones del estado objetivo bajo el subárbol de una ruta específica:

`gnmic {{[-a|--address]}} {{ip:puerto}} {{[sub|subscribe]}} --path {{ruta}}`

- Suscribirse a un objetivo con un intervalo de muestra de 30s (por defecto es 10s):

`gnmic {{[-a|--address]}} {{ip:puerto}} {{[sub|subscribe]}} --path {{ruta}} --sample-interval 30s`

- Suscribirse a un objetivo con intervalo de muestra y actualizaciones solamente cuando hay cambios:

`gnmic {{[-a|--address]}} {{ip:puerto}} {{[sub|subscribe]}} --path {{ruta}} --stream-mode on-change --heartbeat-interval {{1m}}`

- Suscribirse a un objetivo para una sola actualización:

`gnmic {{[-a|--address]}} {{ip:puerto}} {{[sub|subscribe]}} --path {{ruta}} --mode once`

- Suscribirse a un objetivo y especificar la codificación de la respuesta (json_ietf):

`gnmic {{[-a|--address]}} {{ip:puerto}} {{[sub|subscribe]}} --path {{ruta}} {{[-e|--encoding]}} json_ietf`
