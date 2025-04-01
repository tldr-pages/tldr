# medusa

> 一种针对多种协议的模块化并行登录暴力破解工具。
> 更多信息：<https://jmk-foofus.github.io/medusa/medusa.html>。

- 列出所有已安装的模块：

`medusa -d`

- 显示特定模块的使用示例（使用 `medusa -d` 列出所有已安装的模块）：

`medusa -M {{ssh|http|web-form|postgres|ftp|mysql|...}} -q`

- 使用包含用户名和密码的文件对 FTP 服务器执行暴力破解：

`medusa -M ftp -h host -U {{path/to/username_file}} -P {{path/to/password_file}}`

- 使用指定的用户名、密码和用户代理对 HTTP 服务器执行登录尝试：

`medusa -M HTTP -h host -u {{username}} -p {{password}} -m USER-AGENT:"{{Agent}}"`

- 使用包含用户名和哈希的文件对 MySQL 服务器执行暴力破解：

`medusa -M mysql -h host -U {{path/to/username_file}} -p {{hash}} -m PASS:HASH`

- 使用用户名和 pwdump 文件对 SMB 服务器列表执行暴力破解：

`medusa -M smbnt -H {{path/to/hosts_file}} -C {{path/to/pwdump_file}} -u {{username}} -m PASS:HASH`
