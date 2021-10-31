# scan-build

> A command-line utility to run a static analyzer over a codebase as part of performing a regular build.
> More information: <https://clang-analyzer.llvm.org/scan-build.html>.

Basic usage of scan-build is designed to be simple: just place the word `scan-build` in front of your build command:

`scan-build {{make}}`

In the first case scan-build analyzes the code of a project built with `make` and in the second case scan-build analyzes a project built using `xcodebuild`.

Here is the general format for invoking scan-build:

`scan-build [scan-build options] <command> [command options]`

Operationally, scan-build literally runs `<command>` with all of the subsequent options passed to it. For example, one can pass `-j4` to make get a parallel build over 4 cores:

`scan-build make -j4`

In almost all cases, scan-build makes no effort to interpret the options after the build command; it simply passes them through. In general, `scan-build` should support parallel builds, but not distributed builds.

It is also possible to use `scan-build` to analyze specific files:

`scan-build gcc -c t1.c t2.c`

This example causes the files `t1.c` and `t2.c` to be analyzed.
