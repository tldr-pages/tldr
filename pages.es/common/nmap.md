# nmap

> Herramienta de exploración de redes y escáner de seguridad/puertos.
> Algunas funciones (p. ej. escaneo SYN) se activan solamente cuando `nmap` es ejecutado con los permisos del superusuario.
> Más información: <https://nmap.org/book/man.html>.

- Escanea los top 1000 puertos de un host remoto con varios niveles de [v]erbosidad:

`nmap -v{{1|2|3}} {{ip_o_nombre_de_host}}`

- Ejecuta un barrido de ping sobre una subred o hosts específicos:

`nmap -T5 -sn {{192.168.0.0/24|ip_o_nombre_de_host1,ip_o_nombre_de_host2,...}}`

- Activa la detección de sistemas operativos, la detección de versión, el escaneo con guiones y traceroute:

`sudo nmap -A {{ip_o_nombre_de_host1,ip_o_nombre_de_host2,...}}`

- Escanea una lista de puertos (invoca `nmap` con `-p-` para escanear todos los puertos desde 1 a 65535):

`nmap -p {{puerto1,puerto2,...}} {{ip_o_host1,ip_o_host2,...}}`

- Detecta el servicio y versión de los top 1000 puertos usando los guiones NSE por defecto y escribe los resultados (`-oA`) en archivos de salida:

`nmap -sC -sV -oA {{top-1000-ports}} {{ip_o_host1,ip_o_host2,...}}`

- Escanea objetivo(s) cuidadosamente usando los guiones NSE `default and safe`:

`nmap --script "default and safe" {{ip_o_host1,ip_o_host2,...}}`

- Escanea servidores web ejecutándose en los puertos estándares 80 y 443 usando todos los guiones `http-*` NSE disponibles:

`nmap --script "http-*" {{ip_o_host1,ip_o_host2,...}} -p 80,443`

- Intenta evadir los sistemas de detección y prevención de intrusos escaneando extremadamente lento (`-T0`) y usando direcciones de origen de señuelo (`-D`), paquetes [f]ragmentados, datos aleatorios y otros métodos:

`sudo nmap -T0 -D {{ip_de_señuelo1,ip_de_señuelo2,...}} --source-port {{53}} -f --data-length {{16}} -Pn {{ip_o_host}}`
