# env

> Muestra el entorno o ejecuta un programa en un entorno modificado.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- Muestra el entorno:

`env`

- Ejecuta un programa. A menudo se utiliza en scripts después del shebang (#!) para buscar el camino al programa:

`env {{programa}}`

- Limpia el ambiente y ejecuta un programa:

`env {{[-i|--ignore-environment]}} {{programa}}`

- Elimina la variable de entorno y ejecuta un programa:

`env {{[-u|--unset]}} {{variable}} {{programa}}`

- Establece una variable y ejecuta un programa:

`env {{variable}}={{valor}} {{programa}}`

- Establece una o más variables y ejecuta un programa:

`env {{variable1=value variable2=value variable3=value ...}}  {{programa}}`

- Ejecuta un programa con un nombre diferente:

`env {{[-a|--argv0]}} {{nombre_personalizado}} {{programa}}`
