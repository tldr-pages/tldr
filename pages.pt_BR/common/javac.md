# javac

> O compilador de aplicações Java.
> Mais informações: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/javac.html>.

- Compile um arquivo `.java`:

`javac {{arquivo.java}}`

- Compile vários arquivos `.java`:

`javac {{arquivo1.java}} {{arquivo2.java}} {{arquivo3.java}}`

- Compile todos os arquivos `.java` no diretório atual:

`javac {{*.java}}`

- Compile um arquivo `.java` e coloque a classe resultante em um diretório específico:

`javac -d {{caminho/para/diretorio}} {{arquivo.java}}`
