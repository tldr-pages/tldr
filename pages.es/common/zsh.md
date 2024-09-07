# zsh

> Z SHell, un intérprete de línea de comandos compatible con Bash.
> Vea también `histexpand` para la expansión del historial.
> Más información: <https://www.zsh.org>.

- Comienza una sesión interactiva en el intérprete de comandos:

`zsh`

- Ejecuta un comando y sale:

`zsh -c "{{comando}}"`

- Ejecuta un script:

`zsh {{ruta/al/script.zsh}}`

- Comprueba si hay errores de sintaxis en un script sin ejecutarlo:

`zsh --no-exec {{ruta/al/script.zsh}}`

- Ejecuta comandos desde `stdin`:

`{{comando}} | zsh`

- Ejecuta un script, mostrando cada comando antes de ejecutarlo:

`zsh --xtrace {{ruta/al/script.zsh}}`

- Comienza una sesión interactiva en el intérprete de comandos en modo detallado, mostrando cada comando antes de ejecutarlo:

`zsh --verbose`

- Ejecuta un comando dentro de `zsh` con patrones glob desactivados:

`noglob {{command}}`
