# g++

> 编译 C++ 源代码文件。
> 属于 GCC（GNU 编译器集合）。
> 更多信息：<https://gcc.gnu.org>。

- 将源代码文件编译为可执行二进制文件：

`g++ {{path/to/source1.cpp path/to/source2.cpp ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- 激活所有错误和警告的输出：

`g++ {{path/to/source.cpp}} -Wall {{[-o|--output]}} {{output_executable}}`

- 显示常见警告，并在输出中添加调试符号，同时进行不影响调试的优化：

`g++ {{path/to/source.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- 选择要编译的语言标准（C++98/C++11/C++14/C++17）：

`g++ {{path/to/source.cpp}} -std={{c++98|c++11|c++14|c++17}} {{[-o|--output]}} {{path/to/output_executable}}`

- 包含位于不同于源文件路径的库：

`g++ {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- 编译并链接多个源代码文件为一个可执行二进制文件：

`g++ {{[-c|--compile]}} {{path/to/source1.cpp path/to/source2.cpp ...}} && g++ {{[-o|--output]}} {{path/to/output_executable}} {{path/to/source1.o path/to/source2.o ...}}`

- 优化编译的程序以提高性能：

`g++ {{path/to/source.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- 显示版本：

`g++ --version`
