# jar

> Compactador de Bibliotecas e Aplicações Java.
> Mais informações: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- Arquiva recursivamente todos os arquivos do diretório atual em um arquivo .jar:

`jar cf {{file.jar}} *`

- Descompacta o arquivo .jar/.war para o diretório atual:

`jar -xvf {{file.jar}}`

- Lista o conteúdo do arquivo .jar/.war:

`jar tf {{path/to/file.jar}}`

- Lista o conteúdo do arquivo .jar/.war com mais detalhes (verbose):

`jar tvf {{path/to/file.jar}}`
