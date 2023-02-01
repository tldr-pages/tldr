# nc

> Netcat es una utilidad versátil para trabajar con datos TCP o UDP.
> Más información: <https://nmap.org/ncat>.

- Escucha en un puerto determinado e imprime cualquier dato recibido:

`nc -l {{puerto}}`

- Conecta a un puerto determinado:

`nc {{direccion_ip}} {{puerto}}`

- Configura un tiempo máximo de respuesta:

`nc -w {{tiempo_en_segundos}} {{direccion_ip}} {{puerto}}`

- Mantiene el servidor activo hasta que el cliente se desconecte:

`nc -k -l {{puerto}}`

- Mantiene el cliente activo durante un tiempo después de recibir EOF:

`nc -q {{tiempo_en_segundos}} {{direccion_ip}}`

- Escanear puertos abiertos en un determinado host:

`nc -v -z {{direccion_ip}} {{puerto1 puerto2 ...}}`

- Actúa como un proxy y redirige los datos desde un puerto TCP local a un host remoto específico:

`nc -l {{puerto_local}} | nc {{nombre_del_host}} {{puerto_remoto}}`
