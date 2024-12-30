# etckeeper

> 在Git中跟踪系统配置文件。
> 更多信息：<https://etckeeper.branchable.com/>.

- 设置Git仓库并执行各种设置任务（从`/etc`运行）：

`sudo etckeeper init`

- 提交`/etc`中的所有更改：

`sudo etckeeper commit {{message}}`

- 运行任意Git命令：

`sudo etckeeper vcs {{status}}`

- 检查是否有未提交的更改（仅返回退出代码）：

`sudo etckeeper unclean`

- 销毁现有仓库并停止跟踪更改：

`sudo etckeeper uninit`