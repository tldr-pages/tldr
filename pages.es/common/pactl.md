# pactl

> Controla un servidor de sonido PulseAudio en ejecución.
> Más información: <https://manned.org/pactl>.

- Muestra información sobre el servidor de sonido:

`pactl info`

- Lista todos los sinks (u otros tipos - los sinks son salidas y los sink-inputs son flujos de audio activos):

`pactl list {{sinks}} short`

- Cambia el sink (salida) predeterminado a 1 (el número se puede obtener mediante el subcomando `list`):

`pactl set-default-sink {{1}}`

- Mueve el sink-input 627 al sink 1:

`pactl move-sink-input {{627}} {{1}}`

- Establece el volumen del sink 1 al 75%:

`pactl set-sink-volume {{1}} {{0.75}}`

- Cambia el estado de silencio del sink predeterminado (usando el nombre especial `@DEFAULT_SINK@`):

`pactl set-sink-mute {{@DEFAULT_SINK@}} toggle`
