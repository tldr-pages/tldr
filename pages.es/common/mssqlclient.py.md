# mssqlclient.py

> Se conecta a instancias de Microsoft SQL Server y ejecuta consultas.
> Forma parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Se conecta a un servidor MSSQL mediante autenticación de Windows:

`mssqlclient.py -windows-auth {{dominio}}/{{nombre de usuario}}:{{contraseña}}@{{destino}}`

- Se conecta mediante autenticación de SQL Server:

`mssqlclient.py {{nombre de usuario}}:{{contraseña}}@{{destino}}`

- Se conecta mediante autenticación «pass-the-hash»:

`mssqlclient.py {{dominio}}/{{nombre de usuario}}@{{destino}} -hashes {{LM_Hash}}:{{NT_Hash}}`

- Se conecta mediante autenticación Kerberos (requiere tickets válidos):

`mssqlclient.py -k {{dominio}}/{{nombre_de_usuario}}@{{destino}}`

- Ejecuta un comando SQL específico al conectarse:

`mssqlclient.py {{nombre_de_usuario}}:{{contraseña}}@{{destino}} -query "{{SELECT nombre_de_usuario();}}"`

- Ejecutar varios comandos SQL desde un archivo:

`mssqlclient.py {{nombre_de_usuario}}:{{contraseña}}@{{destino}} -file {{ruta/al/archivo_sql.sql}}`

- Se conecta a una instancia de base de datos específica (el valor por defecto es `None`):

`mssqlclient.py {{unombre_de_usuariosername}}:{{contraseña}}@{{destino}} -db {{nombre_base_de_datos}}`

- Muestra las consultas SQL antes de ejecutarlas:

`mssqlclient.py {{nombre_de_usuario}}:{{contraseña}}@{{destino}} -show`
