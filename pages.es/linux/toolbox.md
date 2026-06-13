# toolbox

> Administra entornos de línea de comandos en contenedores en Linux.
> Algunos subcomandos, como `create`, tienen su propia documentación de uso.
> Más información: <https://manned.org/toolbox>.

- Entra en un contenedor Toolbx para utilizarlo de forma interactiva:

`toolbox enter {{contenedor}}`

- Elimina uno o varios contenedores:

`toolbox rm {{contenedor1 contenedor2 ...}}`

- Elimina una o varias imágenes:

`toolbox rmi {{imagen1 imagen2 ...}}`

- Muestra la ayuda para un subcomando específico (como `create`, `enter`, `rm`, etc.):

`toolbox help {{subcomando}}`

- Muestra la ayuda:

`toolbox {{[-h|--help]}}`

- Muestra la versión:

`toolbox --version`
