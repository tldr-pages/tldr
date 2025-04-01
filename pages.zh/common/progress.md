# progress

> 显示/监控正在运行的 coreutils 的进度。
> 更多信息：<https://github.com/Xfennec/progress>.

- 显示正在运行的 coreutils 的进度：

`progress`

- 以静默模式显示正在运行的 coreutils 的进度：

`progress -q`

- 启动并监控单个长时间运行的命令：

`{{command}} & progress --monitor --pid $!`

- 包括对完成时间的估计：

`progress --wait --command {{firefox}}`
