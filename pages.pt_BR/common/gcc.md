# gcc

> Pré-processa e compila arquivos de código fonte C e C++, depois monta-os e vincula-os.
> Mais informações: <https://gcc.gnu.org/onlinedocs/gcc/>.

- Compila múltiplos arquivos de código fonte, produzindo um arquivo executável:

`gcc {{caminho/para/arquivo_fonte1.c caminho/para/arquivo_fonte2.c ...}} {{[-o|--output]}} {{caminho/para/executável_de_saída}}`

- Ativa a saída de todos os erros e avisos:

`gcc {{caminho/para/fonte.c}} -Wall {{[-o|--output]}} {{executável_de_saída}}`

- Mostra avisos comuns, símbolos de depuração na saída, e otimiza sem afetar a depuração:

`gcc {{caminho/para/fonte.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{caminho/para/executável_de_saída}}`

- Inclui bibliotecas de um local diferente:

`gcc {{caminho/para/fonte.c}} {{[-o|--output]}} {{caminho/para/executável_de_saída}} -I{{caminho/para/header}} -L{{caminho/para/biblioteca}} -l{{nome_biblioteca}}`

- Compila o código fonte para instruções Assembler:

`gcc {{[-S|--assemble]}} {{caminho/para/fonte.c}}`

- Compila o código fonte sem efetuar vinculação:

`gcc {{[-c|--compile]}} {{caminho/para/font.c}}`

- Otimiza o programa compilado para desempenho:

`gcc {{caminho/para/fonte.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{caminho/para/executável_de_saída}}`

- Mostra versão:

`gcc --version`
