# phpbu

> 一个适用于 PHP 的备份工具框架。
> 更多信息：<https://phpbu.de>.

- 使用默认的 `phpbu.xml` 配置文件运行备份：

`phpbu`

- 使用特定的配置文件运行备份：

`phpbu --configuration={{path/to/configuration_file.xml}}`

- 仅运行指定的备份任务：

`phpbu --limit={{backup_task_name}}`

- 模拟将要执行的操作：

`phpbu --simulate`