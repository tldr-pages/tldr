# doas

> Ejecuta un comando como otro usuario.
> Vea también: `sudo`, `pkexec`, `run0`.
> Más información: <https://man.openbsd.org/doas>.

- Ejecuta un comando como root:

`doas {{comando}}`

- Ejecuta un comando como otro usuario:

`doas -u {{usuario}} {{comando}}`

- Inicia el intérprete de comandos predeterminado como root:

`doas -s`

- Analiza un archivo de configuración y comprueba si se permite la ejecución de un comando como otro usuario:

`doas -C {{ruta/al/archivo_de_configuración}} {{comando}}`

- Haz que `doas` solicite una contraseña incluso después de haberla proporcionado anteriormente:

`doas -L`
