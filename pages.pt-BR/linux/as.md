# as

> Assembler GNU portável.
> Principalmente destinado a realizar o assemble da saída do `gcc` para ser utilizado pelo `ld`.

- Realiza o assemble de um arquivo, escrevendo a saída em a.out:

`as {{file.s}}`

- Realiza o assemble de um arquivo, escrevendo a saída em um arquivo:

`as {{file.s}} -o {{out.o}}`

- Gera a saída rapidamente, pois ignora o pré-processamento de comentários e espaços em branco. (Deve ser utilizado apenas emr compiladores confiáveis):

`as -f {{file.s}}`

- Adiciona um caminho na lista de diretórios onde será realizada a busca por arquivos especificados na diretiva .include:

`as -I {{path/to/directory}} {{file.s}}`
