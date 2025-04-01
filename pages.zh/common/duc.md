# duc

> 用于索引、检查和可视化磁盘使用情况的工具集。
> Duc 维护了一个文件系统中目录累积大小的数据库，允许查询此数据库，或创建图表以显示数据的位置。
> 更多信息：<http://duc.zevv.nl>。

- 索引 `/usr` 目录，写入默认数据库位置 `~/.duc.db`：

`duc index {{/usr}}`

- 列出 `/usr/local` 下的所有文件和目录，并以图表显示相对文件大小：

`duc ls {{[-Fg|--classify --graph]}} {{/usr/local}}`

- 使用树形视图递归列出 `/usr/local` 下的所有文件和目录：

`duc ls {{[-Fg|--classify --graph]}} {{[-R|--recursive]}} {{/usr/local}}`

- 启动图形界面，使用太阳爆发图探索文件系统：

`duc gui {{/usr}}`

- 运行基于 ncurses 的控制台界面以探索文件系统：

`duc ui {{/usr}}`

- 导出数据库信息：

`duc info`
