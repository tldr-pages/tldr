# htop

> 显示正在运行的进程的动态实时信息。`top` 的增强版。
> 更多信息：<https://htop.dev/>.

- 启动 `htop`:

`htop`

- 启动 `htop`, 显示指定用户拥有的进程：

`htop --user {{用户名}}`

- 使用指定的 `sort_item` 对进程排序（使用 `htop --sort help` 获取可用选项）：

`htop --sort {{sort_item}}`

- 以指定的更新间隔启动 `htop`, 以十分之一秒为单位（即 50 = 5 秒）：

`htop --delay {{50}}`

- 运行 `htop` 时查看交互式命令：

`?`

- 切换到不同的标签：

`tab`

- 显示帮助：

`htop --help`
