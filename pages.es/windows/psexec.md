# psexec

> Ejecutar un proceso de línea de comandos en una máquina remota.
> Este es un comando avanzado y puede ser potencialmente peligroso.
> Más información: <https://learn.microsoft.com/sysinternals/downloads/psexec>.

- Ejecutar un comando usando `cmd` en un shell remoto:

`psexec \\{{host_remoto}} cmd`

- Ejecutar un comando en un host remoto (preautenticado):

`psexec \\{{host_remoto}} -u {{nombre_de_usuario}} -p {{contraseña}}`

- Ejecutar un comando de forma remota y enviar el resultado a un archivo:

`psexec \\{{host_remoto}} cmd /c {{comando}} -an ^>{{ruta\al\archivo.txt}}`

- Ejecutar un programa para interactuar con los usuarios:

`psexec \\{{host_remoto}} -d -i {{nombre_del_programa}}`

- Mostrar la configuración IP del host remoto:

`psexec \\{{host_remoto}} ipconfig /all`
