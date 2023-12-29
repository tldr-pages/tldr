# gcc

> Compilador de arquivos de código fonte C e C++, efetuando também as fases de pré-processamento, assembling e linking.
> Mais informações: <https://gcc.gnu.org>.

- Compila múltiplos arquivos de código fonte, produzindo um arquivo executável:

`gcc {{arquivo_fonte1.c}} {{arquivo_fonte2.c}} --output {{arquivo_executável}}`

- Habilita avisos durante a compilação:

`gcc {{arquivo_fonte.c}} -Wall -Og --output {{arquivo_executável}}`

- Inclui bibliotecas de um local diferente:

`gcc {{arquivo_fonte.c}} --output {{arquivo_executável}} -I{{caminho/para/header}} -L{{caminho/para/biblioteca}} -l{{nome_biblioteca}}`

- Compila o código fonte para instruções Assembler:

`gcc -S {{arquivo_fonte.c}}`

- Compila o código fonte sem efetuar a fase de linking:

`gcc -c {{arquivo_fonte.c}}`
