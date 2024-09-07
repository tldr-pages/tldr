# simplehttpserver

> Un simple servidor HTTP/S que soporta subida de ficheros, autenticación básica y reglas YAML para respuestas personalizadas.
> Una alternativa Go a `http.server` de Python.
> Más información: <https://github.com/projectdiscovery/simplehttpserver>.

- Inicia el servidor HTTP que sirve el directorio actual con salida verbosa (escucha en todas las interfaces y puerto 8000 por defecto):

`simplehttpserver -verbose`

- Inicia el servidor HTTP con autenticación básica sirviendo una ruta específica a través del puerto 80 en todas las interfaces:

`sudo simplehttpserver -basic-auth {{nombre_de_usuario}}:{{contraseña}} -path {{/var/www/html}} -listen 0.0.0.0:80`

- Inicia el servidor HTTP, habilitando HTTPS utilizando un certificado autofirmado con SAN personalizado en todas las interfaces:

`sudo simplehttpserver -https -domain {{*.selfsigned.com}} -listen 0.0.0.0:443`

- Inicia el servidor HTTP con cabeceras de respuesta personalizadas y capacidad de carga:

`simplehttpserver -upload -header '{{X-Powered-By: Go}}' -header '{{Server: SimpleHTTPServer}}'`

- Inicia el servidor HTTP con reglas personalizables en YAML (consulte la documentación para DSL):

`simplehttpserver -rules {{rules.yaml}}`
