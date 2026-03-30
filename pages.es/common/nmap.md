# nmap

> Herramienta de exploración de redes y escáner de puertos/seguridad.
> Algunas funciones (p. ej., escaneo SYN) solo se activan cuando `nmap` se ejecuta con privilegios de root.
> Ver también: `hping3`, `masscan`, `naabu`, `rustscan`, `zmap`.
> Más información: <https://nmap.org/book/man.html>.

- Escanea los 1000 puertos principales de un host remoto con distintos niveles de [v]erbosidad:

`nmap -v{{1|2|3}} {{ip_o_nombre_host}}`

- Realiza un barrido de ping en toda una [s]ub[r]ed o hosts individuales de forma muy agresiva:

`nmap -T5 -sn {{192.168.0.0/24|ip_o_host1,ip_o_host2,...}}`

- Activa detección de SO, de versión, análisis de scripts y traceroute de hosts desde un archivo:

`sudo nmap -A -iL {{ruta/al/archivo.txt}}`

- Escanea una lista específica de [p]uertos (usa `-p-` para todos los puertos del 1 al 65535):

`nmap -p {{puerto1,puerto2,...}} {{ip_o_host1,ip_o_host2,...}}`

- Realiza detección de servicios y versiones en los 1000 puertos principales usando scripts NSE por defecto y escribe los resultados (`-oA`) en archivos de salida:

`nmap -sC -sV -oA {{top-1000-puertos}} {{ip_o_host1,ip_o_host2,...}}`

- Escanea el/los objetivo(s) cuidadosamente usando scripts NSE `default and safe`:

`nmap --script "default and safe" {{ip_o_host1,ip_o_host2,...}}`

- Escanea servidores web en los [p]uertos estándar 80 y 443 usando todos los scripts NSE `http-*` disponibles:

`nmap --script "http-*" {{ip_o_host1,ip_o_host2,...}} -p 80,443`

- Intenta evadir la detección de IDS/IPS usando un escaneo extremadamente lento (`-T0`), direcciones de origen [D]ecoy, paquetes [f]ragmentados, datos aleatorios y otros métodos:

`sudo nmap -T0 -D {{ip_decoy1,ip_decoy2,...}} --source-port {{53}} -f --data-length {{16}} -Pn {{ip_o_host}}`
