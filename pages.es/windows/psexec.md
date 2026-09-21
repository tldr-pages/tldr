# psexec

> Ejecuta un proceso de línea de comandos en una máquina remota.
> Este es un comando avanzado y puede ser potencialmente peligroso.
> Más información: <https://learn.microsoft.com/sysinternals/downloads/psexec>.

- Ejecuta un comando usando `cmd` en un shell remoto:

`psexec \\{{host_remoto}} cmd`

- Ejecuta un comando en un host remoto (preautenticado):

`psexec \\{{host_remoto}} -u {{nombre_de_usuario}} -p {{contraseña}}`

- Ejecuta un comando de forma remota y enviar el resultado a un archivo:

`psexec \\{{host_remoto}} cmd /c {{comando}} -an ^>{{ruta\al\archivo.txt}}`

- Ejecuta un programa para interactuar con los usuarios:

`psexec \\{{host_remoto}} -d -i {{nombre_del_programa}}`

- Mostra la configuración IP del host remoto:

`psexec \\{{host_remoto}} ipconfig /all`
