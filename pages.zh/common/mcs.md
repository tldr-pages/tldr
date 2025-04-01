# mcs

> Mono C# 编译器。
> 更多信息：<https://manned.org/mcs.1>.

- 编译指定的文件：

`mcs {{path/to/input_file1.cs path/to/input_file2.cs ...}}`

- 指定输出程序的名称：

`mcs -out:{{path/to/file.exe}} {{path/to/input_file1.cs path/to/input_file2.cs ...}}`

- 指定输出程序的类型：

`mcs -target:{{exe|winexe|library|module}} {{path/to/input_file1.cs path/to/input_file2.cs ...}}`
