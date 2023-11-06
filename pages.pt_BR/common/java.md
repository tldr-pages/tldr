# java

> Inicializador de programas Java.
> Mais informações: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- Executa um arquivo Java `.class` que contém um método main, usando o nome da classe:

`java {{nome_da_classe}}`

- Executa um programa Java e usa classes adicionais de terceiros ou definidas pelo usuário:

`java -classpath {{caminho/para/classes1}}:{{caminho/para/classes2}}:. {{nome_da_classe}}`

- Executa um programa `.jar`:

`java -jar {{nome_do_arquivo.jar}}`

- Executa um programa `.jar` com o debugger aguardando conexão na porta 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{nome_do_arquivo.jar}}`

- Exiba a versão do JDK, JRE e HotSpot:

`java -version`

- Exiba os comandos disponíveis do Java:

`java -help`
