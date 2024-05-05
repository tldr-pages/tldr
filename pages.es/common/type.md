# type

> Muestra el tipo de comando que ejecutará el intérprete de comandos.
> Nota: todos los ejemplos no son compatibles con POSIX.
> Más información: <https://manned.org/type>.

- Muestra el tipo de un comando:

`type {{comando}}`

- Muestra todas las rutas con el ejecutable especificado (solo funciona en los intérpretes de comandos Bash/fish/Zsh):

`type -a {{comando}}`

- Muestra el nombre del archivo en disco que se ejecutaría (solo funciona en intérpretes de comandos Bash/fish/Zsh):

`type -p {{comando}}`

- Muestra el tipo de un comando específico, alias/palabra clave/función/integrado/archivo (solo funciona en intérpretes de comandos Bash/fish):

`type -t {{comando}}`
