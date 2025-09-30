# arpspoof

> Forja respuestas ARP para interceptar paquetes.
> Más información: <https://manned.org/arpspoof>.

- Envenena todos los hosts para interceptar paquetes en la [i]nterfaz para el host:

`sudo arpspoof -i {{wlan0}} {{ip_del_host}}`

- Envenena el objetivo para interceptar paquetes en la [i]nterfaz para el host:

`sudo arpspoof -i {{wlan0}} -t {{ip_del_objetivo}} {{ip_del_host}}`

- Envenena tanto el objetivo como el host para interceptar paquetes en la [i]nterfaz para el host:

`sudo arpspoof -i {{wlan0}} -r -t {{ip_del_objetivo}} {{ip_del_host}}`
