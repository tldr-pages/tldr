# java

> Lanzador de aplicaciones Java.
> Más información: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html>.

- Ejecuta un archivo Java `.class` que contiene un método principal utilizando solo el nombre de la clase:

`java {{nombreclase}}`

- Ejecutar un programa Java y utilizar clases adicionales de terceros o definidas por el usuario:

`java -classpath {{ruta/a/clases1}}:{{ruta/a/clases2}}:. {{nombreclase}}`

- Ejecutar un programa `.jar`:

`java -jar {{nombrearchivo.jar}}`

- Ejecuta un programa `.jar` con depuración en espera de conexión en el puerto 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{nombrearchivo.jar}}`

- Mostrar las versiones de JDK, JRE y HotSpot:

`java -version`

- Muestra la ayuda:

`java -help`
