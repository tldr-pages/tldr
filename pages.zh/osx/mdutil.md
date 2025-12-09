# mdutil

> 管理 Spotlight（聚焦搜索）用于搜索的索引数据。
> 更多信息：<https://keith.github.io/xcode-man-pages/mdutil.1.html>.

- 显示指定卷（'/'）的索引状态：

`mdutil -s {{/}}`

- 打开 / 关闭给定卷的 Spotlight 索引：

`mdutil -i {{on|off}} {{指定卷文件夹}}`

- 清除索引数据并重新建立索引：

`mdutil -E {{指定卷文件夹}}`
