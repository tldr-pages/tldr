# calibredb

> 操纵电子书数据库。
> 属于 Calibre 电子书库的一部分。
> 更多信息：<https://manual.calibre-ebook.com/generated/en/calibredb.html>。

- 列出库中的电子书及其附加信息：

`calibredb list`

- 搜索并显示电子书的附加信息：

`calibredb list --search {{search_term}}`

- 搜索电子书的 ID：

`calibredb search {{search_term}}`

- 向库中添加一个或多个电子书：

`calibredb add {{path/to/file1 path/to/file2 ...}}`

- 递归添加目录下的所有电子书到库中：

`calibredb add {{[-r|--recurse]}} {{path/to/directory}}`

- 从库中移除一个或多个电子书。需要提供电子书的 ID（见上）：

`calibredb remove {{id1 id2 ...}}`
