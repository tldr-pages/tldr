# gradle

> Gradle es un sistema de código abierto para automatizar la compilación de proyectos
> Más información en: <https://gradle.org>.

- Compilar un proyecto:

`gradle build`

- Excluit la tarea *test*:

`gradle build -x {{test}}`

- Ejecutar en modo offline para prevenir que gradle acceda a la red durante una compilación:

`gradle build --offline`

- Limpiar el directorio de compilación:

`gradle clean`

- Compilar y generar un paquete:

`gradle assembleRelease`
