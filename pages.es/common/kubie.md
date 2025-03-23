# kubie

> Permite saltar entre contextos y espacios de nombre de `kubectl`.
> Más información: <https://github.com/sbstp/kubie>.

- Muestra un menú seleccionable de contextos:

`kubie ctx`

- Cambia el shell actual al contexto dado:

`kubie ctx {{context}}`

- Cambia el shell actual al espacio de nombre dado:

`kubie ns {{namespace}}`

- Cambia el shell actual al contexto y espacio de nombre dados:

`kubie ctx {{context}} -n {{namespace}}`

- Ejecuta un comando en el contexto y espacio de nombre dados, sin crear un nuevo shell:

`kubie exec {{context}} {{namespace}} {{command}}`

- Busca errores en los archivos de configuración de Kubernetes:

`kubie lint`
