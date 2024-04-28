# Tipo

> Muestra el tipo de comando que ejecutará el intérprete de comandos.
> Nota: todos los ejemplos no son compatibles con POSIX.
> Más información: <https://manned.org/type>.

- Muestra el tipo de un comando:

`type {{comando}}`

- Muestra todas las ubicaciones que contienen el ejecutable especificado (sólo funciona en los intérpretes de comandos Bash/fish/Zsh):

`type -a {{comando}}`

- Muestra el nombre del archivo de disco que se ejecutaría (sólo funciona en intérpretes de comandos Bash/fish/Zsh):

`type -p {{comando}}`

- Muestra el tipo de un comando específico, alias/palabra clave/función/builtin/archivo (sólo funciona en intérpretes de comandos Bash/fish):

`type -t {{comando}}`
