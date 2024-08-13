# wafw00f

> Identifica y toma las huellas digitales de los productos Web Application Firewall (WAF) que protegen un sitio web.
> Más información: <https://github.com/EnableSecurity/wafw00f>.

- Comprueba si un sitio web utiliza algún WAF:

`wafw00f {{https://www.ejemplo.com}}`

- Comprueba a todos los WAF detectables sin detenerse en la primera coincidencia:

`wafw00f --findall {{https://www.ejemplo.com}}`

- Pasa peticiones a través de un [p]roxy (como BurpSuite):

`wafw00f --proxy {{http://localhost:8080}} {{https://www.ejemplo.com}}`

- [t]estea un producto WAF específico (ejecuta `wafw00f -l` para obtener una lista de todos los WAF compatibles):

`wafw00f --test {{Cloudflare|Cloudfront|Fastly|ZScaler|...}} {{https://www.ejemplo.com}}`

- Pasa cabeceras personalizadas desde un archivo:

`wafw00f --headers {{ruta/a/cabeceras.txt}} {{https://www.ejemplo.com}}`

- Lee entradas de destino desde un archivo y muestra una salida detallada (múltiples `v` para más verbosidad):

`wafw00f --input {{ruta/a/urls.txt}} -v{{v}}`

- [l]ista todos los WAF que pueden detectarse:

`wafw00f --list`
