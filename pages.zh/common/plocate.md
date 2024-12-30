# plocate

> 快速查找文件名。
> 确保运行 `sudo updatedb` 以包括新文件。
> 更多信息：<https://plocate.sesse.net>。

- 在数据库中查找模式（定期重新计算）：

`plocate {{pattern}}`

- 按确切文件名查找文件（包含不带通配符字符的模式被解释为 `*pattern*`）：

`plocate */{{filename}}`