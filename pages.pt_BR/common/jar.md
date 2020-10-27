# jar

> Compactador de Bibliotecas e Aplicações Java.
> Mais informações: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- Arquiva recursivamente todos os arquivos do diretório atual em um arquivo .jar:

`jar cf {{arquivo.jar}} *`

- Descompacta o arquivo .jar/.war para o diretório atual:

`jar -xvf {{arquivo.jar}}`

- Lista o conteúdo do arquivo .jar/.war:

`jar tf {{caminho/para/arquivo.jar}}`

- Lista o conteúdo do arquivo .jar/.war com mais detalhes (verbose):

`jar tvf {{caminho/para/arquivo.jar}}`
