# crontab

> 为当前用户设置周期性运行的任务。
> 更多信息：<https://crontab.guru/>。

- 编辑当前用户的 crontab 文件：

`crontab -e`

- 编辑指定用户的 crontab 文件：

`sudo crontab -e -u {{user}}`

- 使用给定文件的内容替换当前 crontab：

`crontab {{path/to/file}}`

- 查看当前用户的现有 cron 任务列表：

`crontab -l`

- 删除当前用户的所有 cron 任务：

`crontab -r`

- 每天 10:00 运行的示例任务（* 表示任意值）：

`0 10 * * * {{command_to_execute}}`

- 每 10 分钟运行一次命令的示例 crontab 条目：

`*/10 * * * * {{command_to_execute}}`

- 每周五 2:30 运行指定脚本的示例 crontab 条目：

`30 2 * * Fri {{/absolute/path/to/script.sh}}`
