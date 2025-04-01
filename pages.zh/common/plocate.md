# plocate

> 快速查找文件名。
> 请确保运行 `sudo updatedb` 以包含新文件。
> 更多信息：<https://plocate.sesse.net>.

- 在数据库中查找模式（数据库会定期重新计算）：

`plocate {{pattern}}`

- 通过确切的文件名查找文件（不包含通配符的模式将被解释为 `*pattern*`）：

`plocate */{{filename}}`
