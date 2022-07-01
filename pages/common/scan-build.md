# scan-build

> Command-line utility to run a static analyzer over a codebase as part of performing a regular build.
> More information: <https://clang-analyzer.llvm.org/scan-build.html>.

- Build and analyze the project in the current directory:

`scan-build {{make}}`

- Run a command and pass all subsequent options to it:

`scan-build {{command}} {{command_arguments}}`

- Display help:

`scan-build`
