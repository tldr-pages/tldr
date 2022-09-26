# clang-tidy

> An LLVM-based C/C++ linter to find style violations, bugs and security flaws through static analysis.
> More information: <https://clang.llvm.org/extra/clang-tidy/>.

- Run default checks on a source file:

`clang-tidy {{path/to/file.cpp}}`

- Don't run any checks other than the `cppcoreguidelines` checks on a file:

`clang-tidy {{path/to/file.cpp}} -checks={{-*,cppcoreguidelines-*}}`

- List all available checks:

`clang-tidy -checks={{*}} -list-checks`

- Specify defines and includes as compilation options (after `--`):

`clang-tidy {{path/to/file.cpp}} -- -I{{my_project/include}} -D{{definitions}}`
