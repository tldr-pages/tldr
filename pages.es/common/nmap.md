# nmap

> Herramienta de exploración de redes y escáner de seguridad/puertos.
> Algunas funciones sólo se activan cuando Nmap se ejecuta con privilegios de root.
> Más información: <https://nmap.org/book/man.html>.

- Comprueba si una dirección IP está activa y adivina el sistema operativo del host remoto:

`nmap -O {{ip_o_nombre_del_host}}`

- Intenta determinar si los hosts especificados están activos (exploración ping) y cuáles son sus nombres y direcciones MAC:

`sudo nmap -sn {{ip_o_nombre_del_host}} {{opcional_otra_dirección}}`

- Habilita también los scripts, la detección de servicios, la huella digital del SO y el traceroute:

`nmap -A {{dirección_o_direcciones}}`

- Escanea una lista específica de puertos (usa '-p-' para todos los puertos desde 1 al 65535):

`nmap -p {{port1,port2,...,portN}} {{dirección_o_direcciones}}`

- Realiza la detección de servicios y versiones de los 1000 puertos principales utilizando los scripts por defecto de NSE; escribiendo los resultados ('-oN') en el fichero de salida:

`nmap -sC -sV -oN {{top-1000-puertos.txt}} {{dirección_o_direcciones}}`

- Escanea objetivo(s) cuidadosamente utilizando los scripts NSE "default and safe":

`nmap --script "default and safe" {{dirección_o_direcciones}}`

- Escanea el servidor web que se ejecuta en los puertos estándar 80 y 443 utilizando todos los scripts de NSE 'http-*' disponibles:

`nmap --script "http-*" {{dirección_o_direcciones}} -p 80,443`

- Realiza un escaneo sigiloso muy lento ('-T0') intentando evitar la detección por parte de IDS/IPS y utiliza direcciones IP de origen con señuelo ('-D'):

`nmap -T0 -D {{decoy1_direcciónip,decoy2_direcciónip,...,decoyN_direcciónip}} {{dirección_o_direcciones}}`
