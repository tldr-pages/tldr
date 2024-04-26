# quarkus

> Crea proyectos Quarkus, gestiona extensiones y realiza tareas esenciales de compilación y desarrollo.
> Más información: <https://quarkus.io/guides/cli-tooling>.

- Crea un nuevo proyecto de aplicación en un directorio nuevo:

`quarkus create app {{nombre_del_proyecto}}`

- Ejecuta el proyecto actual en el modo de codificación en vivo:

`quarkus dev`

- Ejecuta la aplicación:

`quarkus run`

- Ejecuta el proyecto actual en modo de prueba continua:

`quarkus test`

- Añade una o más extensiones al proyecto actual:

`quarkus extension add {{nombre_extensión1 nombre_extensión2 ...}}`

- Construye un contenedor de imagen utilizando Docker:

`quarkus image build docker`

- Despliega la aplicación en Kubernetes:

`quarkus deploy kubernetes`

- Actualiza el proyecto:

`quarkus update`
