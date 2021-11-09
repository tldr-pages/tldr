# scan-build

> Command-line utility to run a static analyzer over a codebase as part of performing a regular build.
> More information: <https://clang-analyzer.llvm.org/scan-build.html>.

- Build and analyze the project in the current directory:

`scan-build {{make}}`

- Invoke `scan-build`:

`scan-build [scan-build options] {{command}} [command options]`

- Run a command and pass all subsequent options to it:

`scan-build {{command}} {{arguments}}`

- It is also possible to use `scan-build` to analyze specific files:

`scan-build {{command}}`
