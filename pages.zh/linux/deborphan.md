# deborphan

> 在使用APT包管理器的操作系统上显示孤立包。
> 更多信息：<https://manned.org/deborphan>。

- 显示不被其他包所需要的库包（来自包仓库的“libs”部分）：

`deborphan`

- 列出“libs”部分中的孤立包以及名称看起来像库名称的孤立包：

`deborphan --guess-all`

- 查找仅被其他包推荐或建议（但不被要求）的包：

`deborphan --nice-mode`