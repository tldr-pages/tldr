# GetUserSPNs.py

> Recupera los Service Principal Names (SPNs) asociados a las cuentas de usuario de Active Directory.
> Parte de la suite Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Enumera las cuentas de usuario con un SPN y solicita sus tickets TGS de Kerberos:

`GetUserSPNs.py {{dominio}}/{{nombre_de_usuario}}:{{contraseña}} -dc-ip {{dominio_controlador_ip}}`

- Usa autenticación pass-the-hash:

`GetUserSPNs.py {{dominio}}/{{nombre_de_usuario}} -hashes {{LM_Hash}}:{{NT_Hash}} -dc-ip {{dominio_controlador_ip}}`

- Guarda el resultado en un archivo:

`GetUserSPNs.py {{dominio}}/{{nombre_de_usuario}}:{{contraseña}} -dc-ip {{dominio_controlador_ip}} -outputfile {{ruta/al/archivo_salida}}`

- Pide solo tickets TGS:

`GetUserSPNs.py {{dominio}}/{{nombre_de_usuario}}:{{contraseña}} -dc-ip {{dominio_controlador_ip}} -request`

- Solicita solo tickets TGS utilizando autenticación pass-the-hash:

`GetUserSPNs.py {{dominio}}/{{nombre_de_usuario}} -dc-ip {{dominio_controlador_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} -request`
