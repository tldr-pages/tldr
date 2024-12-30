# ssh-copy-id

> 将您的公钥安装到远程机器的 authorized_keys 中。
> 更多信息：<https://manned.org/ssh-copy-id>。

- 将您的密钥复制到远程机器：

`ssh-copy-id {{username}}@{{remote_host}}`

- 将给定的公钥复制到远程：

`ssh-copy-id -i {{path/to/certificate}} {{username}}@{{remote_host}}`

- 将给定的公钥复制到远程，指定端口：

`ssh-copy-id -i {{path/to/certificate}} -p {{port}} {{username}}@{{remote_host}}`