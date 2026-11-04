# runcon

> Ejecuta un programa en un contexto de seguridad de SELinux diferente.
> Vea también: `secon`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/runcon-invocation.html>.

- Muestra el contexto de seguridad del contexto de ejecución actual:

`runcon`

- Especifica el dominio en el que se ejecutará un comando:

`runcon {{[-t|--type]}} {{dominio}}_t {{comando}}`

- Especifica el rol del contexto con el que se ejecutará un comando:

`runcon {{[-r|--role]}} {{rol}}_r {{comando}}`

- Especifica el contexto completo con el que ejecutar un comando:

`runcon {{usuario}}_u:{{rol}}_r:{{dominio}}_t {{comando}}`
