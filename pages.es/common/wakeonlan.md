# wakeonlan

> Envía paquetes a los PCs habilitados para wake-on-LAN (WOL).
> Más información: <https://manned.org/wakeonlan>.

- Envía paquetes a todos los dispositivos de la red local (255.255.255.255) especificando una dirección MAC:

`wakeonlan {{01:02:03:04:05:06}}`

- Envía paquete a un dispositivo específico a través de una dirección IP:

`wakeonlan {{01:02:03:04:05:06}} {{[-i|--ip]}} {{192.168.178.2}}`

- Imprime los comandos, pero no los ejecutes (dry-run):

`wakeonlan {{[-n|--dry-run]}} {{01:02:03:04:05:06}}`

- Ejecuta en modo silencioso:

`wakeonlan {{[-q|--quiet]}} {{01:02:03:04:05:06}}`
