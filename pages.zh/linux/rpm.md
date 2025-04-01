# rpm

> RPM 软件包管理器。
> 如果想了解其他软件包管理器的等效命令，请参阅：<https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://rpm.org/>。

- 显示 httpd 软件包的版本：

`rpm --query {{httpd}}`

- 列出所有匹配软件包的版本：

`rpm --query --all '{{mariadb*}}'`

- 强制安装软件包，不考虑当前已安装的版本：

`rpm --upgrade {{path/to/package.rpm}} --force`

- 识别文件的所有者并显示软件包的版本：

`rpm --query --file {{/etc/postfix/main.cf}}`

- 列出软件包包含的文件：

`rpm --query --list {{kernel}}`

- 显示 RPM 文件中的脚本片段：

`rpm --query --package --scripts {{package.rpm}}`

- 显示匹配软件包中已更改、缺失或安装不正确的文件：

`rpm --verify --all '{{php-*}}'`

- 显示特定软件包的变更日志：

`rpm --query --changelog {{package}}`
