# duc

> 一套用于索引、检查和可视化磁盘使用情况的工具。
> Duc维护一个文件系统目录的累计大小数据库，允许查询该数据库，或创建精美的图表以显示数据的位置。
> 更多信息：<http://duc.zevv.nl>。

- 索引 /usr 目录，将结果写入默认数据库位置 ~/.duc.db：

`duc index {{/usr}}`

- 列出 /usr/local 下的所有文件和目录，并以 [g]raph 形式显示相对文件大小：

`duc ls -Fg {{/usr/local}}`

- 递归使用树形视图列出 /usr/local 下的所有文件和目录：

`duc ls -Fg -R {{/usr/local}}`

- 启动图形界面，使用太阳爆炸图探索文件系统：

`duc gui {{/usr}}`

- 运行 ncurses 控制台界面以探索文件系统：

`duc ui {{/usr}}`

- 转储数据库信息：

`duc info`