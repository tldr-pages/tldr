# zmap

> Escáner de red rápido y de código abierto para sondeos en toda Internet.
> Vea también: `hping3`, `masscan`, `naabu`, `nmap`, `rustscan`.
> Más información: <https://manned.org/zmap>.

- Escanea una subred o un espacio IPv4 completo para un puerto TCP específico (por defecto: 80):

`zmap {{SUBNETS}} {{[-p|--target-ports]}} {{puerto}}`

- Escanea puertos específicos o rangos de puertos en una subred:

`zmap {{[-p|--target-ports]}} {{puerto1,puerto2-puerto3,...}} {{SUBNETS}}`

- Envía los resultados a un archivo CSV con campos personalizados:

`zmap {{[-o|--output-file]}} {{ruta/al/archivo_salida.csv}} {{[-f|--output-fields]}} "{{saddr,daddr,sport,dport}}" {{SUBNETS}}`

- Limita la velocidad de escaneo a un número específico de paquetes por segundo:

`zmap {{[-r|--rate]}} {{paquetes_por_segundo}} {{SUBNETS}}`

- Realiza un simulacro sin enviar paquetes:

`zmap {{[-d|--dryrun]}} {{SUBNETS}}`

- Excluye subredes utilizando un archivo de lista de bloqueo en notación CIDR:

`zmap {{[-b|--blocklist-file]}} {{ruta/a/blocklist.txt}} {{SUBNETS}}`

- Establece una IP de orígen específica para los paquetes de exploración:

`zmap {{[-S|--source-ip]}} {{ip_origen}} {{SUBNETS}}`

- Limita el número/porcentaje de objetivos a sondear (por ejemplo, 1000 pares IP/puerto):

`zmap {{[-n|--max-targets]}} {{1000}} {{SUBNETS}} {{[-p|--target-ports]}} {{puerto1,puerto2-puerto3}}`
