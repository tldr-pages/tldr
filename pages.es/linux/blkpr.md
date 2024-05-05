# blkpr

> Registra, reserva, libera, anticipa y borra reservas persistentes en un dispositivo de bloque que soporte "Persistent Reservations".
> Más información: <https://manned.org/blkpr>.

- Registra ([c]omando) una nueva reserva con una clave dada en un dispositivo determinado:

`blkpr {{-c|--command}} register --key {{clave_de_reserva}} {{ruta/al/dispositivo}}`

- Establece el [t]ipo de reserva existente en acceso exclusivo:

`blkpr -c reserve -k {{clave_de_reserva}} {{-t|--type}} exclusive-access {{ruta/al/dispositivo}}`

- Adelanta la reserva existente con una clave dada y la reemplaza por una nueva reserva:

`blkpr -c preempt {{-K|--oldkey}} {{clave_antigua}} --key {{nueva_clave}} -t write-exclusive {{ruta/al/dispositivo}}`

- Libera una reserva con una clave y [t]ipo dados en un dispositivo determinado:

`blkpr -c release --key {{clave_de_reserva}} -t {{tipo_de_reserva}} {{ruta/al/dispositivo}}`

- Borra todas las reservas de un dispositivo determinado:

`blkpr -c clear -k {{clave}} {{ruta/al/dispositivo}}`
