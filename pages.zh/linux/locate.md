# locate

> 快速查找文件名。
> 更多信息：<https://manned.org/locate>.

- 在数据库中查找指定模式的文件。注意：数据库会定期重新计算（通常每周或每日）：

`locate {{pattern}}`

- 通过确切的文件名查找文件（不包含通配符的模式将被解释为 `*pattern*`）：

`locate '*/{{filename}}'`

- 重新计算数据库。如果您想要查找最近添加的文件，需要执行此操作：

`sudo updatedb`