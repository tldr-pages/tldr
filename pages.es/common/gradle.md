# gradle

> Gradle es un sistema de código abierto para automatizar la compilación de proyectos
> Más información: <https://gradle.org>.

- Compila un proyecto:

`gradle build`

- Excluye la tarea *test*:

`gradle build -x {{test}}`

- Ejecuta en modo offline para prevenir que gradle acceda a la red durante una compilación:

`gradle build --offline`

- Limpia el directorio de compilación:

`gradle clean`

- Compila y genera un paquete:

`gradle assembleRelease`
