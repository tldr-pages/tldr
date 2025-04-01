# swig

> 生成 C/C++ 代码与各种高级语言（如 JavaScript、Python、C# 等）之间的绑定。
> 它使用特殊的 `.i` 或 `.swg` 文件生成绑定（包含 SWIG 指令的 C/C++ 代码，然后输出包含构建扩展模块所需的所有包装代码的 C/C++ 文件。
> 更多信息：<https://www.swig.org>.

- 生成 C++ 和 Python 之间的绑定：

`swig -c++ -python -o {{path/to/output_wrapper.cpp}} {{path/to/swig_file.i}}`

- 生成 C++ 和 Go 之间的绑定：

`swig -go -cgo -intgosize 64 -c++ {{path/to/swig_file.i}}`

- 生成 C 和 Java 之间的绑定：

`swig -java {{path/to/swig_file.i}}`

- 生成 C 和 Ruby 之间的绑定，并将 Ruby 模块前缀设置为 `foo::bar::`：

`swig -ruby -prefix "{{foo::bar::}}" {{path/to/swig_file.i}}`