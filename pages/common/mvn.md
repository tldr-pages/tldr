# mvn

> Runnign Apache Maven.

- Most common usage is to invoke a life cicle phase:

`mvn package`
`mvn install`
`mvn deploy`

- Invoke more that one phase with arguments:

`mvn clean -P a_profile package clean`

- Running an spring boot project with remote debug:

`mvn spring-boot:run -Drun.jvmArguments="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=5005"`
