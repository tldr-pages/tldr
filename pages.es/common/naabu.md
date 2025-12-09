# naabu

> Un escáner de puertos rápido, escrito en Go, enfocado en fiabilidad y simplicidad.
> Vea también: `nmap`.
> Nota: Algunas características sólo se activan cuando `naabu` se ejecuta con privilegios de superusuario, como el escaneo SYN.
> Más información: <https://docs.projectdiscovery.io/tools/naabu/running>.

- Ejecuta un escaneo SYN contra los puertos predeterminados (top 100) del host remoto:

`sudo naabu -host {{host}}`

- Muestra las interfaces de red disponibles y la dirección IP pública del host local:

`naabu -interface-list`

- Escanea todos los puertos del host remoto (escaneo CONNECT sin `sudo`):

`naabu -p - -host {{host}}`

- Escanea los top 1000 puertos del host remoto:

`naabu -top-ports 1000 -host {{host}}`

- Escanea los puertos TCP 80, 443 y UDP 53 del host remoto:

`naabu -p 80,443,u:53 -host {{host}}`

- Muestra el tipo de CDN que utiliza el host remoto, si existe:

`naabu -p 80,443 -cdn -host {{host}}`

- Ejecuta `nmap` desde `naabu` para contar con funcionalidades adicionales (`nmap` debe estar instalado):

`sudo naabu -v -host {{host}} -nmap-cli 'nmap {{-v -T5 -sC}}'`
