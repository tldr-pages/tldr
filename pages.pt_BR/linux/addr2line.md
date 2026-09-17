# addr2line

> Converte endereços de um binário em nomes de arquivos e números de linha.
> Mais informações: <https://manned.org/addr2line>.

- Exibe o nome do arquivo e o número da linha do código-fonte de um endereço de instrução de um executável:

`addr2line {{[-e|--exe]}} {{caminho/do/executavel}} {{endereco}}`

- Exibe o nome da função, nome do arquivo e número da linha:

`addr2line {{[-e|--exe]}} {{caminho/do/executavel}} {{[-f|--functions]}} {{endereco}}`

- Desembaraça o nome da função em código C++:

`addr2line {{[-e|--exe]}} {{caminho/do/executavel}} {{[-f|--functions]}} {{[-C|--demangle]}} {{endereco}}`
