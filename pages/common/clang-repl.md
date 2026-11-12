# clang-repl

> Read-Eval-Print Loop for C++.
> More information: <https://clang.llvm.org/docs/ClangRepl.html>.

- Start the clang-repl REPL:

`clang-repl`

- Execute a C++ expression:

`clang-repl -e '{{expression}}'`

- Include a header file before starting:

`clang-repl -i {{path/to/header.h}}`

- Specify the C++ standard:

`clang-repl --std={{c++17}}`