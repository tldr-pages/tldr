# gradle

> Un sistema de automatización de construcción de código abierto.
> Más información: <https://gradle.org>.

- Compila un paquete:

`gradle build`

- Excluye la compilación test:

`gradle build -x {{test}}`

- Ejecuta en modo sin conexión para evitar que Gradle acceda a la red durante la compilación:

`gradle build --offline`

- Limpiar el directorio de compilación:

`gradle clean`

- Construye un paquete Android (APK) en modo release:

`gradle assembleRelease`

- Lista las tareas principales:

`gradle tasks`

- Lista todas las tareas:

`gradle tasks --all`
