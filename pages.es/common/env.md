# env

> Muestra el entorno o ejecuta un programa en un entorno modificado.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- Muestra el entorno:

`env`

- Ejecuta un programa. A menudo se utiliza en scripts después del shebang (#!) para buscar la ruta al programa:

`env {{program}}`

- Limpia el entorno y ejecuta un programa:

`env {{[-i|--ignore-environment]}} {{program}}`

- Elimina variable del entorno y ejecuta un programa:

`env {{[-u|--unset]}} {{variable}} {{program}}`

- Establece una variable y ejecuta un programa:

`env {{variable}}={{value}} {{program}}`

- Establece una o más variables y ejecuta un programa:

`env {{variable1=value variable2=value variable3=value ...}} {{program}}`

- Ejecuta un programa con un nombre diferente:

`env {{[-a|--argv0]}} {{custom_name}} {{program}}`
