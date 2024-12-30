# pueue 组

> 显示、添加或删除组。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 显示所有组及其状态和并行任务数量：

`pueue group`

- 添加一个自定义组：

`pueue group --add "{{group_name}}"`

- 删除一个组并将其任务移到默认组：

`pueue group --remove "{{group_name}}"`