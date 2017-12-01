# mvn

> Apache Maven. A build automation tool used for JVM environment projects.

- Most common usage is to invoke a life cicle phase:

`mvn package`

- Invoke more that one phase with arguments:

`mvn clean -P a_profile package clean`

- Ouput all debug information:

`mvn -X clean -P a_profile package clean`

- Use an alternative pom o directory:

`mvn -f path/to/other/pom.xml clean`

- Run a spring boot project with remote debug:

`mvn spring-boot:run -Drun.jvmArguments="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=5005"`
