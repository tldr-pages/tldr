# torsocks

> Enruta el tráfico de cualquier aplicación a través de la red Tor.
> Nota: `torsocks` asumirá que debe conectarse al proxy SOCKS que corre en 127.0.0.1:9050 que es el servicio (daemon) predeterminado de Tor.
> Más información: <https://manned.org/torsocks>.

- Ejecuta un comando usando Tor:

`torsocks {{comando}}`

- Activa o desactiva Tor en este intérprete de comandos:

`. torsocks {{on|off}}`

- Lanza una nueva interfaz de comando habilitada con Tor:

`torsocks --shell`

- Revisa si la interfaz de comando actual está habilitada con Tor (`LD_PRELOAD` este valor estará vacío si no está habilitada):

`torsocks show`

- Aísla el tráfico a través de un circuito Tor diferente, mejorando el anonimato:

`torsocks {{[-i|--isolate]}} {{curl https://check.torproject.org/api/ip}}`

- Se conecta a un proxy Tor que se ejecuta en una dirección y un puerto específico:

`torsocks {{[-a|--address]}} {{ip}} {{[-P|--port]}} {{puerto}} {{comando}}`
