# ufw

> Cortafuegos sin complicaciones (_Uncomplicated Firewall_).
> Interfaz de usuario de iptables para facilitar la configuración de un firewall.
> Más información: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Activa ufw:

`ufw enable`

- Desactiva ufw:

`ufw disable`

- Muestra reglas del ufw, junto con sus números:

`ufw status numbered`

- Permite el tráfico entrante en el puerto 5432 en este host con un comentario que identifique el servicio:

`ufw allow {{5432}} comment "{{servicio}}"`

- Permite sólo el tráfico TCP desde 192.168.0.4 a cualquier dirección de este host, en el puerto 22:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- Deniega tráfico en el puerto 80 en este host:

`ufw deny {{80}}`

- Deniega todo el tráfico al puerto 22:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{22}}`

- Elimina una regla concreta. El número de la regla puede obtenerse del comando `ufw status numbered`:

`ufw delete {{número_de_regla}}`
