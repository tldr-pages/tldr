# cmake

> Cross-platform build system generator.
> It generates Makefiles, Visual Studio projects or others, depending on the target system.

- Generate a Makefile and use it to compile a project in the same directory as the source:

`cmake && make`

- Generate a Makefule and use it to compile a project in a separate directory (out-of-source build):

`cd {{build_dir}} && cmake ../ && make`

- Run cmake in interactive mode (it will ask for each variable, instead of using defaults):

`cmake -i`
