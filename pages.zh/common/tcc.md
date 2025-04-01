# tcc

> 一个小型 C 编译器，可以运行 C 源文件作为脚本，并且命令行选项与 `gcc` 类似。
> 更多信息：<https://bellard.org/tcc/tcc-doc.html>.

- 编译并链接 2 个源文件以生成可执行文件：

`tcc -o {{executable_name}} {{path/to/file1.c}} {{path/to/file2.c}}`

- 直接运行输入文件，就像运行脚本一样，并传递参数给它：

`tcc -run {{path/to/source_file.c}} {{arguments}}`

- 解释包含在文件内的 shebang 的 C 源文件：

`#!{{/full/path/to/tcc}} -run`
