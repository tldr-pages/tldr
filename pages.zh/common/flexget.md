# flexget

> 一个多用途的自动化工具，用于处理内容如种子、nzbs、播客、漫画、系列、电影等。
> 更多信息：<https://flexget.com/en/CLI>。

- 立即运行所有 Flexget 任务：

`flexget execute --now`

- 启动 Flexget 守护进程并将其进程后台化：

`flexget daemon start --daemonize`

- 列出 Flexget 中记录的所有系列：

`flexget series list`

- 从配置文件运行任务：

`flexget -c {{path/to/config.yml}} execute --task {{task_name}}`