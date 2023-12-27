# mvn

> Ferramenta para a criação e gerenciamento de projetos Java.
> Mais informações: <https://maven.apache.org>.

- Compila um projeto:

`mvn compile`

- Cria um artefato de distribuição utilizando o formato espeficado no `pom.xml`, por exemplo o formato `jar`:

`mvn package`

- Cria um artefato de distribuição sem executar testes unitários:

`mvn package -DskipTests`

- Instala um artefato gerado em um repositório local:

`mvn install`

- Apaga artefatos gerados no diretório `target`:

`mvn clean`

- Executa as fases `clean` e `package` em um projeto:

`mvn clean package`

- Executa as fases `clean` e `package` em um projeto utilizando um perfil:

`mvn clean -P{{perfil}} package`

- Executa uma classe que possua o método `main`:

`mvn exec:java -Dexec.mainClass="{{nome.do.pacote.classe}}" -Dexec.args="{{argument1 argument2 ...}}"`
