# apt-key

> Debian 和 Ubuntu 上的 APT 软件包管理器的密钥管理工具。
> 更多信息：<https://manpages.debian.org/latest/apt/apt-key.8.html>.

- 列出可信密钥：

`apt-key list`

- 向可信密钥库中添加一个密钥：

`apt-key add {{密钥文件.asc}}`

- 从可信密钥库中移除一个密钥：

`apt-key del {{密钥 id}}`

- 向可信密钥库中添加一个远程密钥：

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- 指定密钥 ID, 从密钥服务器中添加一个密钥：

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{密钥 id}}`
