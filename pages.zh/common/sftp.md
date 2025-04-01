# sftp

> 安全文件传输程序。
> 通过 SSH 与主机之间进行文件复制的交互式程序。
> 对于非交互式文件传输，请参见 `scp` 或 `rsync`。
> 更多信息：<https://manned.org/sftp>。

- 连接到远程服务器并进入交互命令模式：

`sftp {{remote_user}}@{{remote_host}}`

- 使用备用端口连接：

`sftp -P {{remote_port}} {{remote_user}}@{{remote_host}}`

- 使用预定义主机（在 `~/.ssh/config` 中）连接：

`sftp {{host}}`

- 将远程文件传输到本地系统：

`get {{/path/remote_file}}`

- 将本地文件传输到远程系统：

`put {{/path/local_file}}`

- 递归地将远程目录传输到本地系统（`put` 命令也支持）：

`get -R {{/path/remote_directory}}`

- 获取本地机器上的文件列表：

`lls`

- 获取远程机器上的文件列表：

`ls`