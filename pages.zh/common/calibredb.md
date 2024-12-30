# calibredb

> 操作电子书数据库。
> 是 Calibre 电子书库的一部分。
> 更多信息：<https://manual.calibre-ebook.com/generated/zh/calibredb.html>。

- 列出库中的电子书及附加信息：

`calibredb list`

- 搜索电子书并显示附加信息：

`calibredb list --search {{搜索词}}`

- 仅搜索电子书的 ID：

`calibredb search {{搜索词}}`

- 将一个或多个电子书添加到库中：

`calibredb add {{文件1的路径 文件2的路径 ...}}`

- 递归地将目录下的所有电子书添加到库中：

`calibredb add {{-r|--recurse}} {{目录的路径}}`

- 从库中移除一个或多个电子书。您需要电子书的 ID（见上文）：

`calibredb remove {{id1 id2 ...}}`