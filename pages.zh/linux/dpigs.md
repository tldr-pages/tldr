# dpigs

> 显示在基于 `apt` 的系统中占用最多空间的已安装包。
> 更多信息：<https://manned.org/dpigs>。

- 显示系统中最大的 `n` 个包：

`dpigs {{[-n|--lines]}} {{n}}`

- 使用指定的文件而不是默认的 dpkg 状态文件：

`dpigs {{[-s|--status]}} {{path/to/file}}`

- 显示系统中已安装的二进制包的最大的源代码包：

`dpigs {{[-S|--source]}}`

- 以人类可读的格式显示包大小：

`dpigs {{[-H|--human-readable]}}`

- 显示帮助：

`dpigs {{[-h|--help]}}`
