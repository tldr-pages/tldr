# java

> Inicializador de Programas Java.
> Mais informações: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/java.html>.

- Executa um arquivo Java `.class` que contém um método main, usando o nome da classe:

`java {{nome_da_classe}}`

- Executa um programa `.jar`:

`java -jar {{arquivo.jar}}`

- Executa um programa `.jar`, com o debugger tentando conectar-se na porta 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{arquivo.jar}}`

- Exiba a versão do JDK, JRE e Hotspot:

`java -version`

- Exiba os comandos disponíveis do Java:

`java -help`
