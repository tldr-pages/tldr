# rsync

> 通过默认使用SSH将文件传输到远程主机或从远程主机传输文件（但不能在两个远程主机之间传输）。 
> 要指定远程路径，请使用 `user@host:path/to/file_or_directory`。
> 更多信息：<https://download.samba.org/pub/rsync/rsync.1>。

- 传输文件：

`rsync {{path/to/source}} {{path/to/destination}}`

- 使用归档模式（递归复制目录，复制符号链接而不解析，并保留权限、所有权和修改时间）：

`rsync {{-a|--archive}} {{path/to/source}} {{path/to/destination}}`

- 在发送到目标时压缩数据，显示详细且易读的进度，并在中断时保持部分传输的文件：

`rsync {{-zvhP|--compress --verbose --human-readable --partial --progress}} {{path/to/source}} {{path/to/destination}}`

- 递归复制目录：

`rsync {{-r|--recursive}} {{path/to/source}} {{path/to/destination}}`

- 传输目录内容，但不传输目录本身：

`rsync {{-r|--recursive}} {{path/to/source}}/ {{path/to/destination}}`

- 使用归档模式，解析符号链接，并跳过在目标上较新的文件：

`rsync {{-auL|--archive --update --copy-links}} {{path/to/source}} {{path/to/destination}}`

- 从运行 `rsyncd` 的远程主机传输目录，并删除目标上不存在于源中的文件：

`rsync {{-r|--recursive}} --delete rsync://{{host}}:{{path/to/source}} {{path/to/destination}}`

- 使用不同于默认端口（22）的端口通过SSH传输文件，并显示全局进度：

`rsync {{-e|--rsh}} 'ssh -p {{port}}' --info=progress2 {{host}}:{{path/to/source}} {{path/to/destination}}`