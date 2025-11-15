# java_home

> Devuelve un valor para $JAVA_HOME o ejecuta un comando usando esta variable.
> Más información: <https://www.unix.com/man-page/osx/1/java_home>.

- Lista JVMs basadas en una versión específica:

`java_home --version {{1.5+}}`

- Lista JVMs basadas en una [arch]itectura específica:

`java_home --arch {{i386}}`

- Lista JVMs basadas en tareas específicas (por defecto `CommandLine`):

`java_home --datamodel {{Applets|WebStart|BundledApp|JNI|CommandLine}}`

- Lista JVMs en formato XML:

`java_home --xml`

- Muestra la ayuda:

`java_home --help`
