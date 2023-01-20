# nc

> Netcat es una utilidad versátil para trabajar con datos TCP o UDP.
> Más información: <https://nmap.org/ncat>.

- Escuchar en un puerto determinado e imprimir cualquier dato recibido:

`nc -l {{puerto}}`

- Conectarse a un puerto determinado:

`nc {{direccion_ip}} {{puerto}}`

- Configurar un tiempo máximo de respuesta:

`nc -w {{tiempo_en_segundos}} {{direccion_ip}} {{puerto}}`

- Mantener el servidor activo hasta que el cliente se desconecte:

`nc -k -l {{puerto}}`

- Mantener el cliente activo durante un tiempo después de recibir EOF:

`nc -q {{tiempo_en_segundos}} {{direccion_ip}}`

- Escanear puertos abiertos en un determinado host:

`nc -v -z {{direccion_ip}} {{puerto1 puerto2 ...}}`

- Actuar como un proxy y redirigir los datos desde un puerto TCP local a un host remoto específico:

`nc -l {{puerto_local}} | nc {{nombre_del_host}} {{puerto_remoto}}`
