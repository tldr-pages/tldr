# scp

> 安全复制。
> 使用安全复制协议通过SSH在主机之间复制文件。
> 更多信息：<https://man.openbsd.org/scp>。

- 将本地文件复制到远程主机：

`scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- 在连接远程主机时使用特定端口：

`scp -P {{port}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- 从远程主机复制文件到本地目录：

`scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- 递归地将远程主机的目录内容复制到本地目录：

`scp -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- 在两台远程主机之间复制文件，通过本地主机传输：

`scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_directory}}`

- 在连接远程主机时使用特定用户名：

`scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_directory}}`

- 在与远程主机身份验证时使用特定的SSH私钥：

`scp -i {{~/.ssh/private_key}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- 在连接远程主机时使用特定代理：

`scp -J {{proxy_username}}@{{proxy_host}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`