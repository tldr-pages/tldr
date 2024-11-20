# ant

> Apache Ant: compile e administre projetos baseados em Java.
> Mais informações: <https://ant.apache.org>.

- Compila um projeto com o arquivo padrão de build `build.xml`:

`ant`

- Compila um projeto utilizando um arquivo de build diferente do `build.xml`:

`ant -f {{buildfile.xml}}`

- Printa informações sobre possíveis alvos para este projeto:

`ant -p`

- Printa informações de debug:

`ant -d`

- Executa todos os alvos que não dependem de alvos defeituosos:

`ant -k`
