# nslookup

> Consulta servidores de nombres para varios registros de dominio.
> Vea también: `dig`, `resolvectl`, `host`.
> Más información: <https://manned.org/nslookup>.

- Consulta el servidor de nombres predeterminado del sistema para obtener una dirección IP (registro A) del dominio:

`nslookup {{example.com}}`

- Consulta un servidor de nombres específico para obtener un registro NS del dominio:

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- Consulta una búsqueda inversa (registro PTR) de una dirección IP:

`nslookup -type=PTR {{54.240.162.118}}`

- Consulta cualquier registro disponible usando el protocolo TCP:

`nslookup -vc -type=ANY {{example.com}}`

- Consulta un servidor de nombres específico para obtener el archivo de zona completo (transferencia de zona) del dominio usando el protocolo TCP:

`nslookup -vc -type=AXFR {{example.com}} {{servidor_de_nombres}}`

- Consulta un servidor de correo (registro MX) del dominio mostrando los detalles de la transacción:

`nslookup -type=MX -debug {{example.com}}`

- Consulta un servidor de nombres específico en un número de puerto determinado para obtener un registro TXT del dominio:

`nslookup -port={{número_de_puerto}} -type=TXT {{example.com}} {{servidor_de_nombres}}`
