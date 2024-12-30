# duc

> 一套用于索引、检查和可视化磁盘使用情况的工具。
> Duc 维护了一个文件系统中目录累积大小的数据库，允许查询该数据库，或创建精美的图表以显示数据所在位置。
> 更多信息：<http://duc.zevv.nl>。

- 索引 `/usr` 目录，并写入默认数据库位置 `~/.duc.db`：

`duc index {{/usr}}`

- 列出 `/usr/local` 下的所有文件和目录，以 [g]raph 形式显示相对文件大小：

`duc ls --classify --graph {{/usr/local}}`

- 递归地使用树形视图列出 `/usr/local` 下的所有文件和目录：

`duc ls --classify --graph --recursive {{/usr/local}}`

- 启动图形界面以使用日晷图探索文件系统：

`duc gui {{/usr}}`

- 运行 ncurses 控制台界面以探索文件系统：

`duc ui {{/usr}}`

- 转储数据库信息：

`duc info`