# clang-format

> Formata automaticamente código C/C++/Java/JavaScript/Objective-C/Protobuf/C#.
> Mais informações: <https://clang.llvm.org/docs/ClangFormat.html>.

- Formata um arquivo e exibe o resultado para a `stdout` (saída padrão):

`clang-format {{caminho/para/arquivo}}`

- Formata um arquivo "in-place", ou seja, salvando nele mesmo:

`clang-format -i {{caminho/para/arquivo}}`

- Formata um arquivo usando um estilo de código predefinido:

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} {{caminho/para/arquivo}}`

- Formata um arquivo usando o arquivo `.clang-format` em um dos diretórios pais do arquivo fonte:

`clang-format --style=file {{caminho/para/arquivo}}`

- Gera um arquivo `.clang-format` personalizado:

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} --dump-config > {{.clang-format}}`
