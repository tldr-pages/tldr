# sudo

> Ejecuta un comando como superusuario o como otro usuario.
> Vea también: `pkexec`, `run0`, `doas`.
> Más información: <https://www.sudo.ws/sudo.html>.

- Ejecuta un comando como superusuario:

`sudo {{less /var/log/syslog}}`

- Edita un archivo como superusuario con su editor predeterminado:

`sudo {{[-e|--edit]}} {{/etc/fstab}}`

- Ejecuta un comando como otro usuario y/o grupo:

`sudo {{[-u|--user]}} {{usuario}} {{[-g|--group]}} {{grupo}} {{id -a}}`

- Repite el último comando precedido de `sudo` (solo en Bash, Zsh, etc.):

`sudo !!`

- Inicia el intérprete de comandos predeterminado con privilegios de superusuario y ejecuta los archivos específicos de inicio de sesión (`.profile`, `.bash_profile`, etc.):

`sudo {{[-i|--login]}}`

- Inicia el intérprete de comandos predeterminado con privilegios de superusuario sin cambiar el entorno:

`sudo {{[-s|--shell]}}`

- Inicia el intérprete de comandos predeterminado como el usuario especificado, cargando el entorno del usuario y leyendo los archivos específicos de inicio de sesión (`.profile`, `.bash_profile`, etc.):

`sudo {{[-i|--login]}} {{[-u|--user]}} {{usuario}}`

- Muestra los comandos permitidos (y prohibidos) para el usuario que ejecuta el comando en formato extendido:

`sudo {{[-ll|--list --list]}}`
