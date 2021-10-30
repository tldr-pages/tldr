# g++

> Compiles C++ source files.
> Part of GCC (GNU Compiler Collection).
> More information: <https://gcc.gnu.org>.

- Compile a source code file into an executable binary:

`g++ {{source.cpp}} -o {{output_executable}}`

- Display (almost) all errors and warnings:

`g++ {{source.cpp}} -Wall -o {{output_executable}}`

- Choose a language standard to compile for(C++98/C++11/C++14/C++17):

`g++ {{source.cpp}} -std={{language_standard}} -o {{output_executable}}`

- Include libraries located at a different path than the source file:

`g++ {{source.cpp}} -o {{output_executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`
