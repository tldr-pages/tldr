# pdftk

> Conjunto de utilitários para manipular arquivos PDF.
> Mais informações: <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>.

- Extrai conjuntos de páginas de um arquivo PDF (páginas 1 a 3, 5 e 6 a 10) e guardá-las num novo arquivo:

`pdftk {{arquivo.pdf}} cat {{1-3 5 6-10}} output {{novo_arquivo.pdf}}`

- Concatena uma lista de arquivos PDF, guardando o resultado num novo arquivo:

`pdftk {{arquivo1.pdf arquivo2.pdf arquivoN.pdf ...}} cat output {{novo_arquivo.pdf}}`

- Parte cada página de um arquivo PDF num arquivo separado, com um padrão para o nome dos novos arquivos:

`pdftk {{arquivo.pdf}} burst output {{página_%d.pdf}}`

- Gira em 180° todas as páginas de um arquivo PDF:

`pdftk {{arquivo.pdf}} cat {{1-endsouth}} output {{novo_arquivo.pdf}}`

- Gira a terceira página de um arquivo PDF em 90° no sentido horário, não modificando as restantes:

`pdftk {{arquivo.pdf}} cat {{1-2 3east 4-end}} output {{novo_arquivo.pdf}}`
