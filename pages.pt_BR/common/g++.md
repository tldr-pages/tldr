# gplusplus

> Compilador de arquivos de código fonte C++.
> Parte do GCC (GNU Compiler Collection).
> Mais informações: <https://gcc.gnu.org>.

- Compilar um arquivo de código fonte para um binário executável:

`g++ {{arquivo_fonte.cpp}} -o {{arquivo_executável}}`

- Compilar mostrando todos os erros e avisos:

`g++ {{arquivo_fonte.cpp}} -Wall -o {{arquivo_executável}}`

- Compilar utilizando um padrão específico da linguagem (C++98/C++11/C++14/C++17):

`g++ {{arquivo_fonte.cpp}} -std={{standard_linguagem}} -o {{arquivo_executável}}`

- Compilar incluindo bibliotecas localizadas em um local diferente do arquivo de código fonte:

`g++ {{arquivo_fonte.cpp}} -o {{arquivo_executável}} -I{{caminho/para/header}} -L{{caminho/para/biblioteca}} -l{{nome_biblioteca}}`
