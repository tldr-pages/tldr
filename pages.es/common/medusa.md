# medusa

> Un forzador bruto de inicio de sesión modular y paralelo para una variedad de protocolos.
> Más información: <https://manned.org/medusa>.

- Lista todos los módulos instalados:

`medusa -d`

- Muestra ejemplo de uso de un módulo específico (usa `medusa -d` para listar todos los módulos instalados):

`medusa -M {{ssh|http|web-form|postgres|ftp|mysql|...}} -q`

- Ejecuta fuerza bruta contra un servidor FTP utilizando un fichero que contiene nombres de usuario y un fichero que contiene contraseñas:

`medusa -M ftp -h host -U {{ruta/al/archivo_de_usuario}} -P {{ruta/al/archivo_de_contraseña}}`

- Ejecuta un intento de inicio de sesión contra un servidor HTTP utilizando el nombre de usuario, la contraseña y el agente de usuario especificados:

`medusa -M HTTP -h host -u {{usuario}} -p {{contraseña}} -m USER-AGENT:"{{agente}}"`

- Ejecuta una fuerza bruta contra un servidor MySQL utilizando un fichero que contenga nombres de usuario y un hash:

`medusa -M mysql -h host -U {{ruta/al/archivo_de_usuario}} -p {{hash}} -m PASS:HASH`

- Ejecuta una fuerza bruta contra una lista de servidores SMB utilizando un nombre de usuario y un archivo pwdump:

`medusa -M smbnt -H {{ruta/al/archivo_de_hosts}} -C {{ruta/al/archivo_pwdump}} -u {{usuario}} -m PASS:HASH`
