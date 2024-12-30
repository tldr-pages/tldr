# crontab

> 用于为当前用户调度 cron 任务以按时间间隔运行。
> 更多信息：<https://crontab.guru/>

- 为当前用户编辑 crontab 文件：

`crontab -e`

- 为特定用户编辑 crontab 文件：

`sudo crontab -e -u {{user}}`

- 用给定文件的内容替换当前的 crontab：

`crontab {{path/to/file}}`

- 查看当前用户的现有 cron 任务列表：

`crontab -l`

- 移除当前用户的所有 cron 任务：

`crontab -r`

- 每天 10:00 运行的示例任务 (* 表示任何值)：

`0 10 * * * {{command_to_execute}}`

- 每 10 分钟运行一次命令的示例 crontab 条目：

`*/10 * * * * {{command_to_execute}}`

- 每周五 02:30 运行某个脚本的示例 crontab 条目：

`30 2 * * Fri {{/absolute/path/to/script.sh}}`