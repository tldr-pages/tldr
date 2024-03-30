# as

> Assembler GNU multiplataforma.
> Seu objetivo inicial é realizar o montagem do arquivo gerado pelo `gcc` para ser utilizado pelo `ld`.
> Mais informações: <https://manned.org/as>.

- Realiza a montagem de um arquivo, o resultado dessa operação será gravado no arquivo a.out:

`as {{arquivo.s}}`

- Realiza a montagem de um arquivo, o resultado dessa operação será gravado em um arquivo específico:

`as {{arquivo.s}} -o {{saida.o}}`

- Realiza a montagem de um arquivo rapidamente, pois ignora o pré-processamento de comentários e espaços em branco. (Deve ser utilizado apenas em compiladores confiáveis):

`as -f {{arquivo.s}}`

- Adiciona um caminho na lista de diretórios onde será realizada a busca por arquivos especificados na diretiva .include:

`as -I {{caminho_para_o_diretorio}} {{arquivo.s}}`
