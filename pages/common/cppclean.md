# cppclean

> Find unused code in C++ projects.

- Run in a project's folder:

`cppclean {{path/to/project}}`

- Run on a project where the headers are in the "inc1/" and "inc2/" folders:

`cppclean {{path/to/project}} --include-path={{inc1}} --include-path={{inc2}}`

- Run on a specific file "main.cpp":

`cppclean {{main.cpp}}`

- Run on the current directory, excluding the "build" directory:

`cppclean {{.}} --exclude={{build}}`
