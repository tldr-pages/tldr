# pactree

> Pacman 的软件包依赖树查看工具。
> 更多信息： <https://manned.org/pactree.8>.

- 打印特定软件包的依赖树：

`pactree {{package}}`

- 打印依赖于特定软件包的所有软件包：

`pactree {{[-r|--reverse]}} {{package}}`

- 逐行列出依赖项，跳过重复项：

`pactree {{[-u|--unique]}} {{package}}`

- 包括特定软件包的可选依赖项并彩色显示输出：

`pactree {{[-co|--color --optional]}} {{package}}`

- 显示帮助：

`pactree`