# g++

> Compiles C++ source files.
> Part of GCC (GNU Compiler Collection).
> More information: <https://gcc.gnu.org>.

- Compile a source code file into an executable binary:

`g++ {{path/to/source.cpp}} -o {{path/to/output_executable}}`

- Display (almost) all errors and warnings:

`g++ {{path/to/source.cpp}} -Wall -o {{path/to/output_executable}}`

- Choose a language standard to compile for (C++98/C++11/C++14/C++17):

`g++ {{path/to/source.cpp}} -std={{c++98|c++11|c++14|c++17}} -o {{path/to/output_executable}}`

- Include libraries located at a different path than the source file:

`g++ {{path/to/source.cpp}} -o {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`
