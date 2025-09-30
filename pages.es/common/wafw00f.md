# wafw00f

> Identifica y toma la huella digital de los productos de cortafuegos de aplicaciones web (WAF) que protegen un sitio web.
> Más información: <https://github.com/EnableSecurity/wafw00f/wiki/Usage#arguments-list>.

- Comprueba si un sitio web utiliza algún WAF:

`wafw00f {{https://www.example.com}}`

- Prueba todos los WAF detectables sin detenerte en el primer resultado:

`wafw00f {{[-a|--findall]}} {{https://www.example.com}}`

- Pasa las solicitudes a través de un proxy (como BurpSuite):

`wafw00f {{[-p|--proxy]}} {{http://localhost:8080}} {{https://www.example.com}}`

- Probar un producto WAF específico (ejecutar `wafw00f --list` para obtener una lista de todos los WAF compatibles):

`wafw00f {{[-t|--test]}} {{Cloudflare|Cloudfront|Fastly|ZScaler|...}} {{https://www.example.com}}`

- Pasar encabezados personalizados desde un archivo:

`wafw00f {{[-H|--headers]}} {{path/to/headers.txt}} {{https://www.example.com}}`

- Lee las entradas de destino desde un archivo y muestra una salida detallada (varias `v` para más detalles):

`wafw00f {{[-i|--input]}} {{ruta/a/urls.txt}} -{{vv}}`

- Lista todos los WAF que se pueden detectar:

`wafw00f {{[-l|--list]}}`
