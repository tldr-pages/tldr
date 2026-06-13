# javac

> O compilador de aplicações Java.
> Mais informações: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/javac.html>.

- Compila um arquivo `.java`:

`javac {{arquivo.java}}`

- Compila vários arquivos `.java`:

`javac {{arquivo1.java arquivo2.java ...}}`

- Compila todos os arquivos `.java` no diretório atual:

`javac {{*.java}}`

- Compila um arquivo `.java` e coloque a classe resultante em um diretório específico:

`javac -d {{caminho/para/diretorio}} {{arquivo.java}}`
