# kubie

> Permite saltar entre contextos y espacios de nombres de `kubectl`.
> Más información: <https://github.com/sbstp/kubie>.

- Muestra un menú seleccionable de contextos:

`kubie ctx`

- Cambia el intérprete de comandos actual al contexto dado:

`kubie ctx {{contexto}}`

- Cambia el intérprete de comandos actual al espacio de nombres dado:

`kubie ns {{espacio_de_nombres}}`

- Cambia el intérprete de comandos actual al contexto y espacio de nombres dados:

`kubie ctx {{contexto}} -n {{espacio_de_nombres}}`

- Ejecuta un comando en el contexto y espacio de nombres dados, sin crear un nuevo intérprete de comandos:

`kubie exec {{contexto}} {{espacio_de_nombres}} {{comando}}`

- Busca errores en los archivos de configuración de Kubernetes:

`kubie lint`
