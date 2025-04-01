# crystal

> 管理 Crystal 源代码。
> 更多信息：<https://crystal-lang.org/reference/using_the_compiler>。

- 运行 Crystal 文件：

`crystal {{path/to/file.cr}}`

- 编译文件及其所有依赖项为一个可执行文件：

`crystal build {{path/to/file.cr}}`

- 从命令行或 `stdin` 读取 Crystal 源代码并执行：

`crystal eval '{{code}}'`

- 从 Crystal 文件中的内联文档字符串生成 API 文档：

`crystal docs`

- 编译并运行 Crystal 测试套件：

`crystal spec`

- 启动本地交互式服务器以测试语言：

`crystal play`

- 为 Crystal 应用程序创建项目目录：

`crystal init app {{application_name}}`

- 显示所有帮助选项：

`crystal help`
