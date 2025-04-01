# patator

> 多用途暴力破解工具，具有模块化设计和灵活的使用方式。
> 更多信息：<https://github.com/lanjelot/patator/wiki/Usage>.

- 暴力破解 SSH 登录，带有速率限制和超时选项（成功登录将显示登录横幅或类似信息）：

`patator ssh_login host={{ip_or_host}} user=FILE0 password=FILE1 0={{path/to/users.txt}} 1={{path/to/passwords.txt}} --rate_limit={{seconds}} --timeout={{seconds}} -x ignore:mesg='Authentication failed.'`

- 暴力破解加密的 ZIP 文件：

`patator unzip_pass zipfile={{path/to/file.zip}} password=FILE0 0={{path/to/passwords.txt}} -x ignore:code!=0`

- 暴力破解 HTTP 基本认证（负载文件 `userpass.txt` 应该是 `username:password` 格式）：

`patator http_fuzz url={{http://host:port}} auth_type=basic user_pass=COMBO00:COMBO01 0={{path/to/userpass.txt}} -x ignore:code=401`

- 暴力破解 FTP/FTPS 登录：

`patator ftp_login host={{ip_or_host}} user=FILE0 password=FILE1 0={{path/to/users.txt}} 1={{path/to/passwords.txt}} tls={{0|1}} -x ignore:mesg='Login incorrect.' -x ignore,reset,retry:code=500`

- 列出所有可用模块：

`patator --help`

- 显示特定模块的帮助信息：

`patator {{module_name}} --help`