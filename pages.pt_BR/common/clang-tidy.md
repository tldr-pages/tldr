# clang-tidy

> Um linter C/C++ baseado em LLVM para encontrar violações de estilo, bugs e falhas de segurança por meio de análise estática.
> Mais informações: <https://clang.llvm.org/extra/clang-tidy/>.

- Executa verificações padrão em um arquivo fonte:

`clang-tidy {{caminho/para/arquivo.cpp}}`

- Não executa quaisquer verificações além da verificação `cppcoreguidelines` em um arquivo:

`clang-tidy {{caminho/para/arquivo.cpp}} -checks={{-*,cppcoreguidelines-*}}`

- Lista todas as verificações disponíveis:

`clang-tidy -checks={{*}} -list-checks`

- Especifica defines (definições) e includes (inclusões) como opções de compilações (após `--`):

`clang-tidy {{caminho/para/arquivo.cpp}} -- -I{{meu_projeto/include}} -D{{definições}}`
