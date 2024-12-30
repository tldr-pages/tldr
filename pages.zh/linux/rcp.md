# rcp

> 在本地和远程系统之间复制文件。
> 它模仿 `cp` 命令的行为，但在不同的机器之间操作。
> 更多信息：<https://www.gnu.org/software/inetutils/manual/html_node/rcp-invocation.html>。

- 将文件复制到远程主机：

`rcp {{path/to/local_file}} {{username}}@{{remote_host}}:{{/path/to/destination/}}`

- 递归复制目录：

`rcp -r {{path/to/local_directory}} {{username}}@{{remote_host}}:{{/path/to/destination/}}`

- 保留文件属性：

`rcp -p {{path/to/local_file}} {{username}}@{{remote_host}}:{{/path/to/destination/}}`

- 强制复制不需确认：

`rcp -f {{path/to/local_file}} {{username}}@{{remote_host}}:{{/path/to/destination/}}`