# medusa

> Un forzador bruto de inicio de sesión modular y paralelo para una variedad de protocolos.
> Más información: <https://jmk-foofus.github.io/medusa/medusa.html>.

- Lista todos los módulos instalados:

`medusa -d`

- Muestra ejemplo de uso de un módulo específico (usa `medusa -d` para listar todos los módulos instalados):

`medusa -M {{ssh|http|web-form|postgres|ftp|mysql|...}} -q`

- Ejecuta fuerza bruta contra un servidor FTP utilizando un fichero que contiene nombres de usuario y un fichero que contiene contraseñas:

`medusa -M ftp -h host -U {{ruta/a/archivo_de_nombre_de_usuario}} -P {{ruta/a/archivo_contraseña}}`

- Ejecuta un intento de inicio de sesión contra un servidor HTTP utilizando el nombre de usuario, la contraseña y el agente de usuario especificados:

`medusa -M HTTP -h host -u {{nombre_usuario}} -p {{contraseña}} -m USER-AGENT:"{{Agente}}"`

- Ejecuta una fuerza bruta contra un servidor MySQL utilizando un fichero que contenga nombres de usuario y un hash:

`medusa -M mysql -h host -U {{ruta/a/archivo_de_nombre_de_usuario}} -p {{hash}} -m PASS:HASH`

- Ejecuta una fuerza bruta contra una lista de servidores SMB utilizando un nombre de usuario y un archivo pwdump:

`medusa -M smbnt -H {{ruta/a/archivo_de_hosts}} -C {{ruta/a/archivo_pwdump}} -u {{nombre_usuario}} -m PASS:HASH`
