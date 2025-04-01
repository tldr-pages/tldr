# clamscan

> 命令行病毒扫描器。
> 更多信息：<https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>。

- 扫描文件以查找漏洞：

`clamscan {{path/to/file}}`

- 递归扫描特定目录中的所有文件：

`clamscan -r {{path/to/directory}}`

- 从 `stdin` 扫描数据：

`{{command}} | clamscan -`

- 指定病毒数据库文件或文件目录：

`clamscan --database {{path/to/database_file_or_directory}}`

- 扫描当前目录并仅输出受感染的文件：

`clamscan --infected`

- 将扫描报告打印到日志文件：

`clamscan --log {{path/to/log_file}}`

- 将受感染的文件移动到特定目录：

`clamscan --move {{path/to/quarantine_directory}}`

- 删除受感染的文件：

`clamscan --remove yes`