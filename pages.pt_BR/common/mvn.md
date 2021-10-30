# mvn

> Ferramenta para a criação e gerenciamento de projetos Java.
> Mais informações: <https://maven.apache.org>.

- Compilar um projeto:

`mvn compile`

- Criar um artefato de distribuição utilizando o formato espeficado no `pom.xml`, por exemplo o formato `jar`:

`mvn package`

- Criar um artefato de distribuição sem executar testes unitários:

`mvn package -DskipTests`

- Instalar um artefato gerado em um repositório local:

`mvn install`

- Apagar artefatos gerados no diretório `target`:

`mvn clean`

- Executar as fases `clean` e `package` em um projeto:

`mvn clean package`

- Executar as fases `clean` e `package` em um projeto utilizando um perfil:

`mvn clean -P{{perfil}} package`

- Executar uma classe que possua o método `main`:

`mvn exec:java -Dexec.mainClass="{{nome.do.pacote.classe}}" -Dexec.args="{{arg1 arg2}}"`
