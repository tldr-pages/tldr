# ufw

> Cortafuegos sin complicaciones (_Uncomplicated Firewall_).
> Interfaz de usuario de iptables para facilitar la configuración de un firewall.
> Más información: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Activa ufw:

`ufw enable`

- Desactivar ufw:

`ufw disable`

- Mostrar reglas del ufw, junto con sus números:

`ufw status numbered`

- Permitir el tráfico entrante en el puerto 5432 en este host con un comentario que identifique el servicio:

`ufw allow {{5432}} comment "{{servicio}}"`

- Permitir sólo el tráfico TCP desde 192.168.0.4 a cualquier dirección de este host, en el puerto 22:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{cualquier}} port {{22}}`

- Denegar tráficoen el puerto 80 en este host:

`ufw deny {{80}}`

- Denegar todo el tráfico al puerto 22:

`ufw deny proto {{udp}} from {{cualquier}} to {{cualquier}} port {{22}}`

- Eliminar una regla concreta. El número de la regla puede obtenerse del comando `ufw status numbered`:

`ufw delete {{número_de_regla}}`
