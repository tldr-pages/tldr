# csc

> 微软 C# 编译器。
> 更多信息：<https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>。

- 将一个或多个 C# 文件编译为 CIL 可执行文件：

`csc {{path/to/input_file_a.cs}} {{path/to/input_file_b.cs}}`

- 指定输出文件名：

`csc /out:{{path/to/filename}} {{path/to/input_file.cs}}`

- 编译为 `.dll` 库而不是可执行文件：

`csc /target:library {{path/to/input_file.cs}}`

- 引用另一个程序集：

`csc /reference:{{path/to/library.dll}} {{path/to/input_file.cs}}`

- 嵌入资源：

`csc /resource:{{path/to/resource_file}} {{path/to/input_file.cs}}`

- 自动生成 XML 文档：

`csc /doc:{{path/to/output.xml}} {{path/to/input_file.cs}}`

- 指定图标：

`csc /win32icon:{{path/to/icon.ico}} {{path/to/input_file.cs}}`

- 使用密钥文件强命名生成的程序集：

`csc /keyfile:{{path/to/keyfile}} {{path/to/input_file.cs}}`