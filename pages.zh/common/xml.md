# xml

> XMLStarlet 工具包：查询、编辑、检查、转换和转换 XML 文档。
> 一些子命令，例如 `xml validate`，有其自己的使用文档。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 显示一般帮助，包括子命令列表：

`xml --help`

- 从文件或 URI 执行子命令，输出到 `stdout`：

`xml {{subcommand}} {{options}} {{path/to/input.xml|URI}}`

- 使用 `stdin` 和 `stdout` 执行子命令：

`xml {{subcommand}} {{options}}`

- 从文件或 URI 执行子命令并输出到文件：

`xml {{subcommand}} {{options}} {{path/to/input.xml|URI}} > {{path/to/output}}`

- 显示特定子命令的帮助信息：

`xml {{subcommand}} --help`

- 显示版本信息：

`xml --version`