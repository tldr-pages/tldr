# clamdscan

> 使用 ClamAV 守护进程扫描病毒。
> 更多信息：<https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>。

- 扫描文件或目录中的漏洞：

`clamdscan {{path/to/file_or_directory}}`

- 从 `stdin` 扫描数据：

`{{command}} | clamdscan -`

- 扫描当前目录并仅输出受感染的文件：

`clamdscan --infected`

- 将扫描报告输出到日志文件：

`clamdscan --log {{path/to/log_file}}`

- 将受感染的文件移动到指定目录：

`clamdscan --move {{path/to/quarantine_directory}}`

- 删除受感染的文件：

`clamdscan --remove`

- 使用多个线程扫描目录：

`clamdscan --multiscan`

- 传递文件描述符而不是将文件流式传输到守护进程：

`clamdscan --fdpass`
