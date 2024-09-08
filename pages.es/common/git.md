# git

> Sistema de control de versiones distribuido.
> Algunos subcomandos como `commit`, `add`, `branch`, `checkout`, `push`, etc., tienen su propia documentación de uso.
> Más información: <https://git-scm.com/>.

- Ejecuta un subcomando de Git:

`git {{subcomando}}`

- Ejecuta un subcomando de Git en un repositorio en la ruta raíz especificada:

`git -C {{ruta/al/repositorio}} {{subcomando}}`

- Ejecuta un subcomando de Git con configuración personalizada:

`git -c '{{config.clave}}={{valor}}' {{subcomando}}`

- Muestra ayuda general:

`git --help`

- Muestra ayuda sobre un subcomando de Git (p. ej., `clone`, `add`, `push`, `log`, etc.):

`git help {{subcomando}}`

- Muestra la versión:

`git --version`
