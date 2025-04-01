# xml

> XMLStarlet 工具：查询、编辑、检查、转换和变换 XML 文档。
> 某些子命令（如 `xml validate`）有自己的使用文档。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 显示一般帮助，包括子命令列表：

`xml --help`

- 从文件或 URI 读取输入，执行子命令，并打印到 `stdout`：

`xml {{subcommand}} {{options}} {{path/to/input.xml|URI}}`

- 使用 `stdin` 和 `stdout` 执行子命令：

`xml {{subcommand}} {{options}}`

- 从文件或 URI 读取输入，并将输出写入文件：

`xml {{subcommand}} {{options}} {{path/to/input.xml|URI}} > {{path/to/output}}`

- 显示特定子命令的帮助：

`xml {{subcommand}} --help`

- 显示版本：

`xml --version`