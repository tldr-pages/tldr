# java

> Java Application Launcher.
> More information: <https://java.com>.

- Execute a java .class file that contains a main method by using just the class name:

`java {{classname}}`

- Execute a .jar program:

`java -jar {{filename.jar}}`

- Execute a .jar program with debug waiting to connect on port 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- Display JDK, JRE and HotSpot versions:

`java -version`

- Display usage information for the java command:

`java -help`
