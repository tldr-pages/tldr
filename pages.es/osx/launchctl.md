# launchctl

> Controla el gestor `launchd` de Apple para los programas residentes de inicio (servicios de todo el sistema) y los agentes de inicio (programas específicos de cada usuario).
> `launchd` carga los archivos `*.plist` basados en XML que se encuentran en las ubicaciones adecuadas y ejecuta los comandos correspondientes según la programación definida.
> Más información: <https://keith.github.io/xcode-man-pages/launchctl.1.html>.

- Activa un agente específico del usuario para que se cargue en `launchd` cada vez que el usuario inicie sesión:

`launchctl load ~/Library/LaunchAgents/{{my_script}}.plist`

- Activa un agente que requiera privilegios de root para ejecutarse y/o que deba cargarse cada vez que cualquier usuario inicie sesión (fíjate en la ausencia de `~` en la ruta):

`sudo launchctl load /Library/LaunchAgents/{{root_script}}.plist`

- Activa un programa residente de todo el sistema para que se cargue cada vez que el sistema se inicie (incluso si ningún usuario inicia sesión):

`sudo launchctl load /Library/LaunchDaemons/{{system_daemon}}.plist`

- Muestra todos los agentes/programas residentes cargados, con el PID si el proceso que especifican se está ejecutando actualmente, y el código de salida devuelto la última vez que se ejecutaron:

`launchctl list`

- Descarga un agente cargado actualmente, por ejemplo, para realizar cambios (Nota: el archivo plist se carga automáticamente en `launchd` tras un reinicio o al iniciar sesión):

`launchctl unload ~/Library/LaunchAgents/{{my_script}}.plist`

- Ejecuta manualmente un agente o programa residente conocido (cargado), aunque no sea el momento adecuado (Nota: este comando utiliza la etiqueta del agente, en lugar del nombre del archivo):

`launchctl start {{script_file}}`

- Detiene manualmente el proceso asociado a un agente o programa residente conocido, si se está ejecutando:

`launchctl stop {{script_file}}`
