# etckeeper

> 使用 Git 跟踪系统配置文件。
> 更多信息：<https://etckeeper.branchable.com/>。

- 创建一个 Git 仓库并执行各种初始化任务（从 `/etc` 目录运行）：

`sudo etckeeper init`

- 提交 `/etc` 目录中的所有更改：

`sudo etckeeper commit {{message}}`

- 运行任意 Git 命令：

`sudo etckeeper vcs {{status}}`

- 检查是否有未提交的更改（仅返回退出代码）：

`sudo etckeeper unclean`

- 销毁现有仓库并停止跟踪更改：

`sudo etckeeper uninit`