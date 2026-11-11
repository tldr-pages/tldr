# clang-repl

> Interactive REPL (Read-Evaluate-Print-Loop) environment for C++.
> More information: <https://clang.llvm.org/docs/ClangRepl.html#clang-repl-usage>.

- Run the C++ REPL:

`clang-repl`

- Run C++ from a file:

`clang-repl '#include "{{test.cpp}}"'`

- Run C++ code directly from the command line:

`clang-repl {{'#include <iostream>' 'std::cout << "test\n";' ...}}`

- [Interactive] Evaluate a value:

`{{24|"text"}}`

- [Interactive] Undo the last statement:

`%undo`

- [Interactive] Link a dynamic library:

`%lib {{library.so.1}}`

- [Interactive] Exit the environment:

`{{%quit|<Ctrl c>}}`

- [Interactive] Display help:

`%help`
