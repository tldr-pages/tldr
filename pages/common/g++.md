# g++

> Compile C++ source files.
> Part of GCC (GNU Compiler Collection).
> More information: <https://gcc.gnu.org>.

- Compile a source code file into an executable binary:

`g++ {{path/to/source1.cpp path/to/source2.cpp ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Activate output of all errors and warnings:

`g++ {{path/to/source.cpp}} -Wall {{[-o|--output]}} {{output_executable}}`

- Show common warnings, debug symbols in output, and optimize without affecting debugging:

`g++ {{path/to/source.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- Choose a language standard to compile for (C++98/C++11/C++14/C++17):

`g++ {{path/to/source.cpp}} -std={{c++98|c++11|c++14|c++17}} {{[-o|--output]}} {{path/to/output_executable}}`

- Include libraries located at a different path than the source file:

`g++ {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- Compile and link multiple source code files into an executable binary:

`g++ {{[-c|--compile]}} {{path/to/source1.cpp path/to/source2.cpp ...}} && g++ {{[-o|--output]}} {{path/to/output_executable}} {{path/to/source1.o path/to/source2.o ...}}`

- Optimize the compiled program for performance:

`g++ {{path/to/source.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- Display version:

`g++ --version`
