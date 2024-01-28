# jbang

> Crea, edita y ejecuta fácilmente programas en Java autocontenidos de sólo código fuente.
> Ver también: `java`.
> Más información: <https://www.jbang.dev/documentation/guide/latest/cli/jbang.html>.

- Inicializa una clase Java simple:

`jbang init {{ruta/al/archivo.java}}`

- Inicializa una clase Java (útil para scripts):

`jbang init --template={{cli}} {{ruta/al/archivo.java}}`

- Utiliza `jshell` para explorar y utilizar un script y cualquier dependencia en un editor REPL:

`jbang run --interactive`

- Configura un proyecto temporal para editar un script en un IDE:

`jbang edit --open={{codium|code|eclipse|idea|netbeans|gitpod}} {{ruta/al/script.java}}`

- Ejecuta un fragmento de código Java (Java 9 y posteriores):

`{{echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'}} | jbang -`

- Ejecuta aplicación de línea de comandos:

`jbang {{ruta/al/archivo.java}} {{comando}} {{arg1 arg2 ...}}`

- Instala un script en el `$PATH` del usuario:

`jbang app install --name {{nombre_del_comando}} {{ruta/al/script.java}}`

- Instala una versión específica del JDK para utilizarla con `jbang`:

`jbang jdk install {{versión}}`
