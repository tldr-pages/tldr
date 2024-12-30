# nxc ftp

> 渗透测试和利用FTP服务器。
> 更多信息：<https://www.netexec.wiki/ftp-protocol>。

- 通过尝试指定的用户名和密码列表中的每一种组合来搜索有效凭据：

`nxc ftp {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 即使在找到有效凭据后，仍继续搜索有效凭据：

`nxc ftp {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}} --continue-on-success`

- 对所有有效凭据的每个FTP服务器执行目录列表：

`nxc ftp {{192.168.178.0/24}} -u {{username}} -p {{password}} --ls`

- 从目标服务器下载指定的文件：

`nxc ftp {{192.168.178.2}} -u {{username}} -p {{password}} --get {{path/to/file}}`

- 将指定的文件上传到目标服务器的指定位置：

`nxc ftp {{192.168.178.2}} -u {{username}} -p {{password}} --put {{path/to/local_file}} {{path/to/remote_location}}`