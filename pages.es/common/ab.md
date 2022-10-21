# ab

> Herramienta comparativa del servidor Apache HTTP.
> Más información: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Ejecuta 100 solicitudes HTTP GET a una URL dada:

`ab -n {{100}} {{url}}`

- Ejecuta 100 solicitudes HTTP GET, en lotes simultáneos de a 10, a una URL:

`ab -n {{100}} -c {{10}} {{url}}`

- Ejecuta 100 solicitudes HTTP POST a una URL, utilizando la carga JSON de un archivo:

`ab -n {{100}} -T {{application/json}} -p {{ruta/al/archivo.json}} {{url}}`

- Utiliza HTTP [K]eep Alive, es decir, realiza múltiples solitudes dentro de una sesión HTTP:

`ab -k {{url}}`

- Establece el máximo número de segundos utilizados para la comparación:

`ab -t {{60}} {{url}}`
