# pacdiff

> 用于处理由 `pacman` 生成的 `.pacorig`、`.pacnew` 和 `.pacsave` 文件的维护工具。
> 更多信息：<https://manned.org/pacdiff>.

- 以交互模式审查需要维护的文件：

`pacdiff`

- 使用 sudo 和 sudoedit 删除和合并文件：

`pacdiff --sudo`

- 审查需要维护的文件，如果选择 `(O)verwrite` 则为原始文件创建 `.bak` 备份：

`pacdiff --sudo --backup`

- 使用特定的编辑器查看和合并配置文件（默认为 `vim -d`）：

`DIFFPROG={{editor}} pacdiff`

- 使用 `locate` 而不是 `pacman` 数据库来查找配置文件：

`pacdiff --locate`

- 显示帮助：

`pacdiff --help`
