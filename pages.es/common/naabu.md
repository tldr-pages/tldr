# naabu

> Un escáner de puertos rápido escrito en Go que se centra en la fiabilidad y la simplicidad.
> Nota: Algunas funciones solo se activan cuando `naabu` se ejecuta con privilegios de root, como el escaneo SYN.
> Vea también: `hping3`, `masscan`, `nmap`, `rustscan`, `zmap`.
> Más información: <https://docs.projectdiscovery.io/opensource/naabu/running>.

- Ejecuta un escaneo SYN en los puertos predeterminados (los 100 principales) del host remoto:

`sudo naabu -host {{host}}`

- Muestra las interfaces de red disponibles y la dirección IP pública del host local:

`naabu {{[-il|-interface-list]}}`

- Escanea todos los puertos del host remoto (escaneo CONNECT sin `sudo`):

`naabu {{[-p|-port]}} - -host {{host}}`

- Escanea los 1000 puertos principales del host remoto:

`naabu {{[-tp|-top-ports]}} 1000 -host {{host}}`

- Escanea los puertos TCP 80, 443 y el puerto UDP 53 del host remoto:

`naabu {{[-p|-port]}} 80,443,u:53 -host {{host}}`

- Muestra el tipo de CDN que utiliza el host remoto, si lo hay:

`naabu {{[-p|-port]}} 80,443 -cdn -host {{host}}`

- Ejecuta `nmap` desde `naabu` para obtener funcionalidades adicionales (`nmap` debe estar instalado):

`sudo naabu {{[-v|-verbose]}} -host {{host}} -nmap-cli "nmap {{-v -T5 -sC}}"`
