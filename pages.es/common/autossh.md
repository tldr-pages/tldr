# autossh

> Ejecuta, monitorea y reinicia conexiones SSH.
> Auto-reconecta para mantener los túneles de reenvío de puertos. Acepta todas las señales SSH.
> Más información: <https://www.harding.motd.ca/autossh>.

- Inicia una sesión SSH, reiniciando cuando un puerto de monitoreo no retorna datos:

`autossh -M {{puerto_monitor}} "{{comando_ssh}}"`

- Reenvía un puerto local a uno remoto, reiniciando cuando sea necesario:

`autossh -M {{puerto_monitor}} -L {{puerto_local}}:localhost:{{puerto_remoto}} {{usuario}}@{{host}}`

- Crea un proceso `autossh` en segundo plano antes de ejecutar SSH y no abre un shell remoto:

`autossh -f -M {{puerto_monitor}} -N "{{comando_ssh}}"`

- Ejecuta en segundo plano, sin puerto de monitorización, y en su lugar envía paquetes SSH keep-alive cada 10 segundos para detectar fallos:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{comando_ssh}}"`

- Ejecuta en segundo plano, sin puerto de monitorización y sin shell remoto, saliendo si falla el reenvío de puerto:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{puerto_remoto}} {{usuario}}@{{host}}`

- Se ejecuta en segundo plano, registrando la salida de depuración `autossh` y la salida detallada SSH en archivos:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{ruta/al/autossh_log_file.log}} autossh -f -M {{puerto_monitor}} -v -E {{ruta/al/archivo_ssh_log.log}} {{comando_ssh}}`
