# nmap

> Herramienta de exploración de redes y escáner de seguridad / puertos.
> Algunas características solo funcionan si ejecutamos Nmap con privilegios.
> Más información: <https://nmap.org>.

- Comprueba si una dirección IP está activa, e intenta averiguar el sistema operativo del servidor correspondiente:

`nmap -O {{ip_o_hostname}}`

- Intenta determinar si los hosts están activos y cuáles son sus nombres:

`nmap -sn {{ip_o_hostname}} {{opcional_otra_direccion}}`

- Como el anterior, pero también ejecuta un escaneo de 1000 puertos TCP por defecto, si el host está activo:

`nmap {{ip_o_hostname}} {{opcional_otra_direccion}}`

- Detecta también scripts, servicios, sistema operativo y traceroute:

`nmap -A {{direccion_o_direcciones}}`

- Asume una buena conexión y acelera la ejecución:

`nmap -T4 {{direccion_o_direcciones}}`

- Escanea una lista específica de puertos (para todos los puertos `1-65535` usar `-p-`):

`nmap -p {{puerto1,puerto2,…,puertoN}} {{direccion_o_direcciones}}`

- Realiza un escaneo TCP y UDP (usar `-sU` para solo UDP, `-sZ` para SCTP, `-sO` para IP):

`nmap -sSU {{direccion_o_direcciones}}`

- Realiza un escaneo total de puertos, servicios, detección de versiones con todos los scripts NSE por defecto contra un host para determinar debilidades e información:

`nmap -sC -sV {{direccion_o_direcciones}}`
