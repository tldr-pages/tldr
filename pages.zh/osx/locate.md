# locate

> 快速查找文件名。
> 更多信息：<https://keith.github.io/xcode-man-pages/locate.1.html>。

- 在数据库中查找模式。注意：数据库会定期重新计算（通常是每周或每天）：

`locate "{{pattern}}"`

- 通过精确文件名查找文件（不包含通配符字符的模式将被解释为 `*pattern*`）：

`locate */{{filename}}`

- 重新计算数据库。如果您想查找最近添加的文件，您需要执行此操作：

`sudo /usr/libexec/locate.updatedb`