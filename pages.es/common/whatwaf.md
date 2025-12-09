# whatwaf

> Detecta y elude cortafuegos de aplicaciones web y sistemas de protección.
> Más información: <https://github.com/Ekultek/WhatWaf#basic-help-menu>.

- Detecta protección en una sola [u]RL, opcionalmente utiliza salida verbose:

`whatwaf --url {{https://example.com}} --verbose`

- Detecta protección en un [l]ista de URLs en paralelo desde un archivo (una URL por línea):

`whatwaf --threads {{número}} --list {{ruta/a/archivo}}`

- Envía peticiones a través de un proxy y utiliza una lista de carga útil personalizada desde un archivo (una carga útil por línea):

`whatwaf --proxy {{http://127.0.0.1:8080}} --pl {{ruta/a/archivo}} -u {{https://example.com}}`

- Envía peticiones a través de Tor (Tor debe estar instalado) utilizando cargas personalizadas (separadas por comas):

`whatwaf --tor --payloads '{{carga1,carga2,...}}' -u {{https://example.com}}`

- Utiliza un agente de usuario aleatorio, establece el estrangulamiento y el tiempo de espera, envía una solicitud [P]OST y fuerza una conexión HTTPS:

`whatwaf --ra --throttle {{segundos}} --timeout {{segundos}} --post --force-ssl -u {{http://example.com}}`

- Enumera todos los WAF que se pueden detectar:

`whatwaf --wafs`

- Lista todos los scripts de manipulación disponibles:

`whatwaf --tampers`
