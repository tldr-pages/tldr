# clang

> Compila arquivos fonte escritos em C, C++ e Objective-C. Pode ser usado como um substituto drop-in para GCC.
> Parte de LLVM.
> Mais informações: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compila vários arquivos fonte para um executável:

`clang {{caminho/para/arquivo_fonte1.c caminho/para/arquivo_fonte2.c ...}} {{[-o|--output]}} {{caminho/para/executável_resultante}}`

- Ativa a saída de todos os erros e avisos:

`clang {{caminho/para/arquivo_fonte.c}} -Wall {{[-o|--output]}} {{executável_resultante}}`

- Mostra avisos comuns, faz depuração de símbolos na saída e otimiza sem afetar a depuração:

`clang {{caminho/para/arquivo_fonte.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{caminho/para/executável_resultante}}`

- Inclui bibliotecas de um caminho diferente:

`clang {{caminho/para/arquivo_fonte.c}} {{[-o|--output]}} {{caminho/para/executável_resultante}} -I{{caminho/para/cabeçalho}} -L{{caminho/para/biblioteca}} -l{{nome_da_biblioteca}}`

- Compila o código-fonte na Representação Intermediária (IR) do LLVM:

`clang {{[-S|--assemble]}} -emit-llvm {{caminho/para/arquivo_fonte.c}} {{[-o|--output]}} {{path/to/output.ll}}`

- Compila o código-fonte em um arquivo objeto sem vincular:

`clang {{[-c|--compile]}} {{caminho/para/arquivo_fonte.c}}`

- Otimiza o programa compilado para desempenho:

`clang {{caminho/para/arquivo_fonte.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{caminho/para/executável_resultante}}`

- Exibe a versão:

`clang --version`
