# ant

> Apache Ant: compila e administra projetos baseados em Java.
> Mais informações: <https://ant.apache.org/manual/index.html>.

- Compila um projeto com o arquivo padrão de build `build.xml`:

`ant`

- Compila um projeto utilizando um arquivo de build diferente do `build.xml`:

`ant -f {{arquivo_de_build.xml}}`

- Mostra informações sobre possíveis alvos para este projeto:

`ant -p`

- Mostra informações de debug:

`ant -d`

- Executa todos os alvos que não dependem de alvos defeituosos:

`ant -k`
