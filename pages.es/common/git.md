# git

> Sistema de control de versiones distribuido.
> Algunos subcomandos, como `commit`, `add`, `branch`, `checkout`, `push`, etc., tienen su propia documentación de uso, accessible a través de `tldr git subcomando`.
> Más información: <https://git-scm.com/>.

- Muestra la versión de Git:

`git --version`

- Muestra ayuda general:

`git --help`

- Muestra ayuda sobre un subcomando de Git (como `clone`, `add`, `push`, `log`, etc.):

`git help {{subcomando}}`

- Ejecuta un subcomando de Git:

`git {{subcomando}}`

- Ejecuta un subcomando de Git en un repositorio en la ruta raíz especificada:

`git -C {{ruta/al/repositorio}} {{subcomando}}`

- Ejecuta un subcomando de Git con la configuración definida:

`git -c '{{config.clave}}={{valor}}' {{subcomando}}`
