# pabcnetcclear

> 预处理和编译 PascalABC.NET 源文件。
> 更多信息：<https://pascalabc.net>.

- 将指定的源文件编译为同名的可执行文件：

`pabcnetcclear {{path\to\source_file.pas}}`

- 将指定的源文件编译为指定名称的可执行文件：

`pabcnetcclear /Output:{{path\to\_file.exe}} {{path\to\source_file.pas}}`

- 将指定的源文件编译为同名的可执行文件，包含/不包含调试信息：

`pabcnetcclear /Debug:{{0|1}} {{path\to\source_file.pas}}`

- 在编译源文件时允许在指定路径中搜索单元：

`pabcnetcclear /SearchDir:{{path\to\directory}} {{path\to\source_file.pas}}`

- 编译指定的源文件，并定义一个符号：

`pabcnetcclear /Define:{{symbol}} {{path\to\source_file.pas}}`