# mdutil

> 管理 Spotlight 用于索引的元数据存储。
> 更多信息：<https://keith.github.io/xcode-man-pages/mdutil.1.html>。

- 显示启动卷的索引状态：

`mdutil -s {{/}}`

- 打开/关闭指定卷的 Spotlight 索引：

`mdutil -i {{on|off}} {{path/to/volume}}`

- 打开/关闭所有卷的索引：

`mdutil -a -i {{on|off}}`

- 擦除元数据存储并重新启动索引过程：

`mdutil -E {{path/to/volume}}`