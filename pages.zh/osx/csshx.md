# csshX

> 用于 macOS 的集群 SSH 工具。
> 更多信息：<https://github.com/brockgr/csshx>.

- 连接到多个主机：

`csshX {{hostname1}} {{hostname2}}`

- 使用指定的 SSH 密钥连接到多个主机：

`csshX {{user@hostname1}} {{user@hostname2}} --ssh_args "-i {{path/to/key_file.pem}}"`

- 从 `/etc/clusters` 中连接到预定义的集群：

`csshX cluster1`
