# secretsdump.py

> Vuelca hashes NTLM, contraseñas en texto plano y credenciales de dominio de sistemas Windows remotos.
> Parte de la suite Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Vuelca credenciales de una máquina Windows utilizando un nombre de usuario y una contraseña:

`secretsdump.py {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{objetivo}}`

- Vuelca hashes de una máquina utilizando autenticación pass-the-hash:

`secretsdump.py -hashes {{LM_Hash}}:{{NT_Hash}} {{dominio}}/{{nombre_de_usuario}}@{{destino}}`

- Vuelca credenciales del archivo NTDS.dit de Active Directory:

`secretsdump.py -just-dc {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{destino}}`

- Extrae credenciales de una base de datos SAM local utilizando archivos hives del registro:

`secretsdump.py -sam {{ruta/a/SAM}} -system {{ruta/a/SYSTEM}}`

- Vuelca hashes de una máquina sin proporcionar una contraseña (si existe una sesión de autenticación válida, por ejemplo, a través de Kerberos o NTLM SSO):

`secretsdump.py -no-pass {{dominio}}/{{nombre_usuario}}@{{destino}}`
