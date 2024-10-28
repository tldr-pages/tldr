# torsocks

> Enruta el tráfico de cualquier aplicación a través de la red Tor.
> Nota: `torsocks` asumirá que debe conectarse al proxy Tor SOCKS que se ejecuta en 127.0.0.1:9050 siendo los valores por defecto del daemon Tor.
> Más información: <https://gitlab.torproject.org/tpo/core/torsocks/>.

- Ejecuta un comando usando Tor:

`torsocks {{comando}}`

- Activa o desactiva Tor en este intérprete de comandos:

`. torsocks {{on|off}}`

- Crea un nuevo intérprete de comandos Tor habilitado:

`torsocks --shell`

- Comprueba si el intérprete de comandos actual está habilitado para Tor (el valor `LD_PRELOAD` estará vacío si está deshabilitado):

`torsocks show`

- A[i]sla el tráfico a través de un circuito Tor diferente, mejorando el anonimato:

`torsocks --isolate {{curl https://check.torproject.org/api/ip}}`

- Se conecta a un proxy Tor que se ejecuta en una dirección específica y [p]uerto:

`torsocks --address {{ip}} --port {{puerto}} {{comando}}`
