# pactree

> pacman 的软件包依赖树查看器。
> 更多信息：<https://manned.org/pactree.8>。

- 打印特定软件包的依赖树：

`pactree {{package}}`

- 打印哪些软件包依赖于特定软件包：

`pactree --reverse {{package}}`

- 每行打印一个依赖项，跳过重复项：

`pactree --unique {{package}}`

- 包括特定软件包的可选依赖项并为输出着色：

`pactree --optional --color {{package}}`

- 显示帮助信息：

`pactree`