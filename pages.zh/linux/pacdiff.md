# pacdiff

> 用于维护由 `pacman` 创建的 `.pacorig`、`.pacnew` 和 `.pacsave` 文件的实用程序。
> 更多信息：<https://manned.org/pacdiff>。

- 以交互模式查看需要维护的文件：

`pacdiff`

- 使用 sudo 和 sudoedit 删除和合并文件：

`pacdiff --sudo`

- 查看需要维护的文件，如果你选择 `(O)verwrite`，则会创建原始文件的 `.bak` 备份：

`pacdiff --sudo --backup`

- 使用特定编辑器查看和合并配置文件（默认是 `vim -d`）：

`DIFFPROG={{editor}} pacdiff`

- 使用 `locate` 扫描配置文件，而不是使用 `pacman` 数据库：

`pacdiff --locate`

- 显示帮助信息：

`pacdiff --help`