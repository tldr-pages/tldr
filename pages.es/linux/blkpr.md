# blkpr

> Registra, reserva, libera, anticipa y borra reservas persistentes en un dispositivo de bloque que soporte "Persistent Reservations".
> Más información: <https://manned.org/blkpr>.

- Registra (comando) una nueva reserva con una clave dada en un dispositivo determinado:

`blkpr {{-c|--command}} register {{-k|--key}} {{clave_de_reserva}} {{ruta/al/dispositivo}}`

- Establece el tipo de reserva existente en acceso exclusivo:

`blkpr -c reserve {{-k|--key}} {{clave_de_reserva}} {{-t|--type}} exclusive-access {{ruta/al/dispositivo}}`

- Adelanta la reserva existente con una clave dada y la reemplaza por una nueva reserva:

`blkpr -c preempt {{-K|--oldkey}} {{clave_antigua}} {{-k|--key}} {{nueva_clave}} {{-t|--type}} write-exclusive {{ruta/al/dispositivo}}`

- Libera una reserva con una clave y [t]ipo dados en un dispositivo determinado:

`blkpr -c release {{-k|--key}} {{clave_de_reserva}} {{-t|--type}} {{tipo_de_reserva}} {{ruta/al/dispositivo}}`

- Borra todas las reservas de un dispositivo determinado:

`blkpr -c clear {{-k|--key}} {{clave}} {{ruta/al/dispositivo}}`
