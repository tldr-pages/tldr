# deborphan

> 在使用 APT 包管理器的操作系统上显示孤儿包。
> 更多信息：<https://manned.org/deborphan>.

- 显示没有被其他包依赖的库包（来自包仓库的“libs”部分）：

`deborphan`

- 列出“libs”部分的孤儿包以及名称看起来像库名的孤儿包：

`deborphan --guess-all`

- 查找仅被其他包推荐或建议（但不被依赖）的包：

`deborphan --nice-mode`
