# nmap

> Herramienta de exploración de redes y escáner de seguridad/puertos.
> Algunas funciones (por ejemplo, el escaneo SYN) solo se activan cuando se ejecuta `nmap` con privilegios de root.
> Vea también: `hping3`, `masscan`, `naabu`, `rustscan`, `zmap`.
> Más información: <https://nmap.org/book/man.html>.

- Escanea los 1000 puertos principales de un host remoto con varios niveles de [v]erbosidad:

`nmap -v{{1|2|3}} {{ip_o_nombre_del_host}}`

- Ejecuta un barrido de ping sobre toda una [s]ub[n]et o hosts individuales de forma muy agresiva:

`nmap -T5 -sn {{192.168.0.0/24|ip_o_nombre_de_host1,ip_o_nombre_de_host2,...}}`

- Habilita la detección del sistema operativo, la detección de la versión, el escaneo de scripts y el traceroute de los hosts desde un archivo:

`sudo nmap -A -iL {{ruta/al/archivo.txt}}`

- Escanea una lista específica de puertos (usa `-p-` para todos los puertos del 1 al 65535):

`nmap -p {{puerto1,puerto2,...}} {{ip_o_host1,ip_o_host2,...}}`

- Realiza la detección de servicios y versiones de los 1000 puertos principales utilizando scripts NSE predeterminados, escribiendo los resultados (`-oA`) en archivos de salida:

`nmap -sC -sV -oA {{top-1000-ports}} {{ip_or_host1,ip_or_host2,...}}`

- Escanea los objetivos cuidadosamente utilizando scripts NSE "predeterminados y seguros":

`nmap --script «default and safe» {{ip_o_host1,ip_o_host2,...}}`

- Escanea los servidores web que se ejecutan en los puertos estándar 80 y 443 utilizando todos los scripts NSE "http-*" disponibles:

`nmap --script "http-*" {ip_o_host1,ip_o_host2,...}} -p 80,443`

- Intente evadir la detección de IDS/IPS utilizando un escaneo extremadamente lento (`-T0`), direcciones de origen [D]e señuelo, paquetes [f]ragmentados, datos aleatorios y otros métodos:

`sudo nmap -T0 -D {{decoy_ip1,decoy_ip2,...}} --source-port {{53}} -f --data-length {{16}} -Pn {ip_o_host}`
