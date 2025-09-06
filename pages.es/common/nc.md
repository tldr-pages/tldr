# nc

> Redirige datos de entrada o salida a un flujo de red a través de esta versátil herramienta.
> Más información: <https://manned.org/nc>.

- Inicia un escuchador en un puerto TCP y le envía un archivo:

`nc -l -p {{puerto}} < {{nombre_de_archivo}}`

- Conecta a un escuchador en un puerto y recibe un archivo de él:

`nc {{host}} {{puerto}} > {{nombre_de_archivo_por_recibir}}`

- Escanea los puertos TCP abiertos en un host:

`nc -v -z -w {{tiempo_de_espera_en_segundos}} {{host}} {{puerto_inicial}}-{{puerto_final}}`

- Inicia un escuchador en un puerto TCP y provee de acceso a tu intérprete de comandos local a la parte conectada (esto es peligroso y podría ser explotado):

`nc -l -p {{puerto}} -e {{ejecutable_del_intérprete}}`

- Conecta a un escuchador y provee de acceso a tu intérprete de comandos local a una parte remota (esto es peligroso y podría ser explotado):

`nc {{host}} {{puerto}} -e {{ejecutable_del_intérprete}}`

- Actúa como un proxy y envía información de un puerto TCP local a un host remoto:

`nc -l -p {{puerto_local}} | nc {{host}} {{puerto_remoto}}`

- Envía una petición HTTP GET:

`echo -e "GET / HTTP/1.1\nHost: {{host}}\n\n" | nc {{host}} 80`
