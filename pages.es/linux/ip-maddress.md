# ip maddress

> Gestiona direcciones multicast.
> Más información: <https://manned.org/ip-maddress>.

- Lista las direcciones multicast y cuántos programas están suscritos a ellas:

`ip maddress`

- Lista de direcciones específicas de dispositivos:

`ip maddress show dev {{eth0}}`

- Se une a un grupo multicast estáticamente:

`sudo ip maddress add {{33:33:00:00:00:02}} dev {{eth0}}`

- Abandona un grupo multicast estático:

`sudo ip maddress delete {{33:33:00:00:00:02}} dev {{eth0}}`
