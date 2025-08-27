# crontab

> 为当前用户计划 cron 任务，按照时间间隔运行。
> 更多信息：<https://manned.org/crontab>.

- 编辑当前用户的 crontab 文件：

`crontab -e`

- 为特定用户修改 crontab 文件：

`sudo crontab -e -u {{用户}}`

- 用指定文件的内容，覆盖当前的 crontab 文件：

`crontab {{路径/到/文件}}`

- 查看当前用户，现存的 cron 任务列表：

`crontab -l`

- 移除当前用户的所有 cron 任务：

`crontab -r`

- 每天 10:00 运行任务的示例（* 表示任意值）：

`0 10 * * * {{要_运行的_命令}}`

- 每 10 分钟运行命令的 crontab 任务条目示例：

`*/10 * * * * {{要_运行的_命令}}`

- 每周五的 02:30 运行指定脚本的 crontab 任务条目示例：

`30 2 * * Fri /{{路径/到/脚本.sh}}`
