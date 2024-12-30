# 美杜莎

> 一种针对多种协议的模块化和并行登录暴力破解工具。
> 更多信息：<https://jmk-foofus.github.io/medusa/medusa.html>。

- 列出所有已安装的模块：

`medusa -d`

- 显示特定模块的用法示例（使用 `medusa -d` 列出所有已安装的模块）：

`medusa -M {{ssh|http|web-form|postgres|ftp|mysql|...}} -q`

- 针对FTP服务器执行暴力破解，使用包含用户名的文件和包含密码的文件：

`medusa -M ftp -h host -U {{path/to/username_file}} -P {{path/to/password_file}}`

- 针对HTTP服务器执行登录尝试，使用指定的用户名、密码和用户代理：

`medusa -M HTTP -h host -u {{username}} -p {{password}} -m USER-AGENT:"{{Agent}}"`

- 针对MySQL服务器执行暴力破解，使用包含用户名的文件和哈希值：

`medusa -M mysql -h host -U {{path/to/username_file}} -p {{hash}} -m PASS:HASH`

- 针对一组SMB服务器执行暴力破解，使用用户名和pwdump文件：

`medusa -M smbnt -H {{path/to/hosts_file}} -C {{path/to/pwdump_file}} -u {{username}} -m PASS:HASH`