# naabu

> Un rápido escáner de puertos escrito en Go con un enfoque en la fiabilidad y la simplicidad.
> Nota: Algunas características solo se activan cuando `naabu` se ejecuta con privilegios del superusuario, como el escaneo SYN.
> Más información: <https://github.com/projectdiscovery/naabu>.

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
