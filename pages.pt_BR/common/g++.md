# g++

> Compila arquivos de código fonte C++.
> Parte do GCC (GNU Compiler Collection).
> Mais informações: <https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html>.

- Compila um arquivo de código fonte para um binário executável:

`g++ {{caminho/para/fonte1.cpp caminho/para/fonte1.cpp ...}} {{[-o|--output]}} {{caminho/para/executável_de_saída}}`

- Ativa saída de todos os erros e avisos:

`g++ {{caminho/para/fonte.css}} -Wall {{[-o|--output]}} {{executável_de_saída}}`

- Mostra avisos comuns, símbolos de depuração na saída, e otimiza sem afetar a depuração:

`g++ {{caminho/para/fonte.cpp}} -Wall {{-g|--debug}} -Og {{[-o|--output]}} {{caminho/para/executável_de_saída}}`

- Escolhe um padrão de linguagem para o qual compilar (C++98/C++11/C++14/C++17):

`g++ {{caminho/para/fonte.cpp}} -std={{c++98|c++11|c++14|c++17}} {{[-o|--output]}} {{caminho/para/executável_de_saída}}`

- Inclui bibliotecas localizadas em um caminho diferente do arquivo de código fonte:

`g++ {{caminho/para/fonte.cpp}} {{[-o|--output]}} {{caminho/para/executável_de_saída}} -I{{caminho/para/cabeçalho}} -L{{caminho/para/biblioteca}} -l{{nome_da_biblioteca}}`

- Compila e vincula múltiplos arquivos de código fonte em um binário executável:

`g++ {{-c|--compile}} {{caminho/para/fonte1.cpp caminho/para/fonte2.cpp ...}} && g++ {{[-o|--output]}} {{caminho/para/executável_de_saída}} {{caminho/para/fonte1.o caminho/para/fonte2.o ...}}`

- Otimiza o programa compilado para desempenho:

`g++ {{caminho/para/fonte.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{caminho/para/executavel_de_saída}}`

- Exibe versão:

`g++ --version`
