# sudo

> Ejecuta un único comando como superusuario u otro usuario.
> Vea también: `pkexec`, `run0`, `doas`.
> Más información: <https://www.sudo.ws/sudo.html>.

- Ejecuta un comando como superusuario:

`sudo {{less /var/log/syslog}}`

- Edita un archivo como superusuario con tu editor predeterminado:

`sudo {{[-e|--edit]}} {{/etc/fstab}}`

- Ejecuta un comando como otro usuario y/o grupo:

`sudo {{[-u|--user]}} {{usuario}} {{[-g|--group]}} {{grupo}} {{id -a}}`

- Repite el último comando prefijado con `sudo` (solo en Bash, Zsh, etc.):

`sudo !!`

- Inicia el shell predeterminado con privilegios de superusuario y ejecuta los archivos específicos de inicio de sesión (`.profile`, `.bash_profile`, etc.):

`sudo {{[-i|--login]}}`

- Inicia el shell predeterminado con privilegios de superusuario sin cambiar el entorno:

`sudo {{[-s|--shell]}}`

- Inicia el shell predeterminado como el usuario especificado, cargando su entorno y leyendo los archivos de inicio de sesión (`.profile`, `.bash_profile`, etc.):

`sudo {{[-i|--login]}} {{[-u|--user]}} {{usuario}}`

- Lista los comandos permitidos (y prohibidos) para el usuario que lo invoca en formato detallado:

`sudo {{[-ll|--list --list]}}`
