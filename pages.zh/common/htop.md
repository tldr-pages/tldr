# htop

> 显示正在运行的进程的动态实时信息。`top` 的增强版。
> 更多信息：<https://manned.org/htop>.

- 启动 `htop`:

`htop`

- 启动 `htop`, 显示指定用户拥有的进程：

`htop {{[-u|--user]}} {{用户名}}`

- 以树形视图显示进程的层级关系，展示父子进程之间的关系：

`htop {{[-t|--tree]}}`

- 使用指定的 `sort_item` 对进程排序（使用 `htop --sort help` 获取可用选项）：

`htop {{[-s|--sort]}} {{sort_item}}`

- 以指定的更新间隔启动 `htop`, 以十分之一秒为单位（即 50 = 5 秒）：

`htop {{[-d|--delay]}} {{50}}`

- 运行 `htop` 时查看交互式命令：

`<?>`

- 切换到不同的标签：

`<Tab>`

- 显示帮助：

`htop {{[-h|--help]}}`
