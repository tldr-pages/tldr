# as

> Assembler GNU multiplataforma.
> Seu objetivo inicial é realizar o montagem do arquivo gerado pelo `gcc` para ser utilizado pelo `ld`.
> Mais informações: <https://manned.org/as>.

- Realiza a montagem de um arquivo, o resultado dessa operação será gravado no arquivo a.out:

`as {{caminho/para/arquivo.s}}`

- Realiza a montagem de um arquivo, o resultado dessa operação será gravado em um arquivo específico:

`as {{caminho/para/arquivo.s}} -o {{caminho/para/saida.o}}`

- Realiza a montagem de um arquivo rapidamente, pois ignora o pré-processamento de comentários e espaços em branco. (Deve ser utilizado apenas em compiladores confiáveis):

`as -f {{caminho/para/arquivo.s}}`

- Adiciona um caminho na lista de diretórios onde será realizada a busca por arquivos especificados na diretiva .include:

`as -I {{caminho_para_o_diretorio}} {{caminho/para/arquivo.s}}`
