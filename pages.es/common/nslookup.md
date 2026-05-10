# nslookup

> Consulta los servidores de nombres para obtener diversos registros de dominio.
> Vea también: `dig`, `resolvectl`, `host`.
> Más información: <https://manned.org/nslookup>.

- Consulta al servidor de nombres predeterminado de tu sistema la dirección IP (registro A) del dominio:

`nslookup {{example.com}}`

- Consulta un servidor de nombres determinado para obtener un registro NS del dominio:

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- Realiza una consulta de búsqueda inversa (registro PTR) de una dirección IP:

`nslookup -type=PTR {{54.240.162.118}}`

- Consulta CUALQUIER registro disponible utilizando el protocolo TCP:

`nslookup -vc -type=ANY {{example.com}}`

- Consulta un servidor de nombres determinado para obtener el archivo de zona completo (transferencia de zona) del dominio utilizando el protocolo TCP:

`nslookup -vc -type=AXFR {{example.com}} {{nombre_servidor}}`

- Consulta un servidor de correo (registro MX) del dominio, mostrando los detalles de la transacción:

`nslookup -type=MX -debug {{example.com}}`

- Consulta un servidor de nombres determinado en un número de puerto específico para obtener un registro TXT del dominio:

`nslookup -port={{número_puerto}} -type=TXT {{example.com}} {{nombre_servidor}}`
