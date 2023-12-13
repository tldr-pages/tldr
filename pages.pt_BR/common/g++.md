# g++

> Compila arquivos de código fonte C++.
> Parte do GCC (GNU Compiler Collection).
> Mais informações: <https://gcc.gnu.org>.

- Compilar um arquivo de código fonte para um binário executável:

`g++ {{caminho/para/fonte.cpp}} -o {{caminho/para/executável_de_saída}}`

- Exibe avisos comuns:

`g++ {{caminho/para/fonte.cpp}} -Wall -o {{caminho/para/executável_de_saída}}`

- Escolha um padrão de linguagem para o qual compilar (C++98/C++11/C++14/C++17):

`g++ {{caminho/para/fonte.cpp}} -std={{c++98|c++11|c++14|c++17}} -o {{caminho/para/executável_de_saída}}`

- Inclui bibliotecas localizadas em um caminho diferente do arquivo de código fonte:

`g++ {{caminho/para/fonte.cpp}} -o {{caminho/para/executável_de_saída}} -I{{caminho/para/cabeçalho}} -L{{caminho/para/biblioteca}} -l{{nome_da_biblioteca}}`

- Compila e vincula múltiplos arquivos de código fonte em um binário executável:

`g++ -c {{caminho/para/fonte_1.cpp caminho/para/fonte_2.cpp ...}} && g++ -o {{caminho/para/executável_de_saída}} {{caminho/para/fonte_1.o caminho/para/fonte_2.o ...}}`

- Exibe versão:

`g++ --version`
