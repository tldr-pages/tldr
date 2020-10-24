# cmake

> Cross-platform build system generator.
> It generates Makefiles, Visual Studio projects or others, depending on the target system.
> More information: <https://cmake.org/cmake/help/v3.2/manual/cmake.1.html>.

- Generate a Makefile and use it to compile a project in the same directory as the source:

`cmake && make`

- Generate a Makefile and use it to compile a project in a separate "build" directory (out-of-source build):

`cmake -H. -B{{build}} && make -C {{build}}`
