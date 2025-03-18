# clang++

> Compila arquivos fonte escritos em C++.
> Parte de LLVM.
> Mais informações: <https://clang.llvm.org>.

- Compila um conjunto de arquivos do código-fonte para um executável binário:

`clang++ {{caminho/para/arquivo_fonte1.cpp caminho/para/arquivo_fonte2.cpp ...}} {{[-o|--output]}} {{caminho/para/executável_resultante}}`

- Ativa a saída de todos os erros e avisos:

`clang++ {{caminho/para/arquivo_fonte.cpp}} -Wall {{[-o|--output]}} {{executável_resultante}}`

- Mostra avisos comuns, faz depuração de símbolos na saída e otimiza sem afetar a depuração:

`clang++ {{caminho/para/arquivo_fonte.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{caminho/para/executável_resultante}}`

- Escolhe um padrão da linguagem para o qual deve-se compilar:

`clang++ {{caminho/para/arquivo_fonte.cpp}} -std={{c++20}} {{[-o|--output]}} {{caminho/para/executável_resultante}}`

- Inclui bibliotecas localizadas em um caminho diferente do arquivo fonte:

`clang++ {{caminho/para/arquivo_fonte.cpp}} {{[-o|--output]}} {{caminho/para/executável_resultante}} -I{{caminho/para/cabeçalho}} -L{{caminho/para/biblioteca}} -l{{caminho/para/nome_da_biblioteca}}`

- Compila o código-fonte na Representação Intermediária (IR) do LLVM:

`clang++ {{[-S|--assemble]}} -emit-llvm {{caminho/para/arquivo_fonte.cpp}} {{[-o|--output]}} {{caminho/para/saída.ll}}`

- Otimiza o programa compilado para desempenho:

`clang++ {{caminho/para/arquivo_fonte.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{caminho/para/executável_resultante}}`

- Exibe a versão:

`clang++ --version`
