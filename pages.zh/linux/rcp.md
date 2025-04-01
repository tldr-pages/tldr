# rcp

> 在本地和远程系统之间复制文件。
> 它模仿 `cp` 命令的行为，但可以在不同的机器之间操作。
> 更多信息：<https://www.gnu.org/software/inetutils/manual/html_node/rcp-invocation.html>.

- 将文件复制到远程主机：

`rcp {{path/to/local_file}} {{username}}@{{remote_host}}:{{/path/to/destination/}}`

- 递归复制目录：

`rcp {{[-r|--recursive]}} {{path/to/local_directory}} {{username}}@{{remote_host}}:{{/path/to/destination/}}`

- 保持文件属性：

`rcp {{[-p|--preserve]}} {{path/to/local_file}} {{username}}@{{remote_host}}:{{/path/to/destination/}}`

- 强制复制，不进行确认：

`rcp {{[-f|--from]}} {{path/to/local_file}} {{username}}@{{remote_host}}:{{/path/to/destination/}}`
