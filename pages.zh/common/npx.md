# npx

> 执行来自 `npm` 包的二进制文件。
> 更多信息：<https://github.com/npm/npx>。

- 从本地或远程 `npm` 包中执行命令：

`npx {{command}} {{argument1 argument2 ...}}`

- 如果存在多个同名命令，可以显式指定包：

`npx --package {{package}} {{command}}`

- 如果命令在当前路径或 `node_modules/.bin` 中存在，则运行该命令：

`npx --no-install {{command}} {{argument1 argument2 ...}}`

- 执行特定命令并抑制 `npx` 本身的任何输出：

`npx --quiet {{command}} {{argument1 argument2 ...}}`

- 显示帮助信息：

`npx --help`