# apt-key

> Debian和Ubuntu上的APT软件包管理器的密钥管理工具

- 列出可信密钥:

`apt-key list`

- 向可信密钥库中添加一个密钥:

`apt-key add {{密钥文件.asc}}`

- 从可信密钥库中移除一个密钥:

`apt-key del {{密钥id}}`

- 向可信密钥库中添加一个远程密钥:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- 指定密钥ID,从密钥服务器中添加一个密钥:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{密钥id}}`
