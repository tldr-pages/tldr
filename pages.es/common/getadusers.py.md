# GetADUsers.py

> Recupera una lista de usuarios de Active Directory, incluyendo atributos como la fecha y hora del último inicio de sesión y el correo electrónico.
> Parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Enumera todos los usuarios de Active Directory y sus atributos:

`GetADUsers.py -all -dc-ip {{ip_controlador_dominio}} {{dominio}}/{{nombre_usuario}}:{{contraseña}}`

- Recupera información solo para un usuario específico:

`GetADUsers.py -user {{usuario}} -dc-ip {{ip_controlador_dominio}} {{dominio}}/{{nombre_usuario}}:{{contraseña}}`

- Extrae los detalles del usuario utilizando la autenticación pass-the-hash:

`GetADUsers.py -all -dc-ip {{ip_controlador_dominio}} -hashes {{LM_Hash}}:{{NT_Hash}} {{dominio}}/{{nombre_usuario}}`

- Guarda la salida en un archivo:

`GetADUsers.py -all -dc-ip {{ip_controlador_dominio}} {{dominio}}/{{nombre_usuario}}:{{contraseña}} > {{ruta/a/salida.txt}}`
