# rsync

> 一种快速，通用，远程（和本地）文件复制工具，默认使用 SSH。
> 如果要指定远程路径，请使用 `user@host:path/to/file_or_directory`.
> 更多信息：<https://download.samba.org/pub/rsync/rsync.1>.

- 复制文件：

`rsync {{路径/到/来源}} {{路径/到/目标}}`

- 使用归档模式递归拷贝文件，并保留所有属性，不解析软链接：

`rsync --archive {{路径/到/来源}} {{路径/到/目标}}`

- 将文件以归档模式并保留几乎所有属性进行传输，并以人类可读方式输出详细信息和进度条，中断时保留部分信息：

`rsync --compress --verbose --human-readable --partial --progress {{路径/到/来源}} {{路径/到/目标}}`

- 以递归模式传输文件：

`rsync --recursive {{路径/到/来源}} {{路径/到/目标}}`

- 将目录下的所有内容（不包含该目录），以递归方式传输：

`rsync --recursive {{路径/到/来源}}/ {{路径/到/目标}}`

- 归档方式传输目录，保留几乎所有属性，解析软连接，并忽略已传输的文件：

`rsync --archive --update --copy-links {{路径/到/来源}} {{路径/到/目标}}`

- 传输目录到运行 `rsyncd` 的远端，并删除目标目录中源目录中不存在的文件：

`rsync --recursive --delete rsync://{{host}}:{{路径/到/来源}} {{路径/到/目标}}`

- 指定本地和远程之间通信方式，使用指定端口，并显示进度条：

`rsync --rsh 'ssh -p {{端口}}' --info=progress2 {{host}}:{{路径/到/来源}} {{路径/到/目标}}`
