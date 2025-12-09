# evtest

> Muestra información de los controladores de dispositivos de entrada.
> Más información: <https://manned.org/evtest>.

- Lista todos los dispositivos de entrada detectados:

`sudo evtest`

- Muestra los eventos de un dispositivo de entrada específico:

`sudo evtest /dev/input/event{{número}}`

- Agarra el dispositivo exclusivamente, evitando que otros clientes reciban eventos:

`sudo evtest --grab /dev/input/event{{número}}`

- Consulta el estado de una tecla o botón específico en un dispositivo de entrada:

`sudo evtest --query /dev/input/event{{número}} {{tipo_evento}} {{código_evento}}`
