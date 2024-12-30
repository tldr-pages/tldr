# rpm

> RPM 包管理器。
> 有关其他包管理器中等效命令的信息，请参见 <https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息请访问：<https://rpm.org/>。

- 显示 httpd 包的版本：

`rpm --query {{httpd}}`

- 列出所有匹配包的版本：

`rpm --query --all '{{mariadb*}}'`

- 强制安装一个包，不考虑当前已安装的版本：

`rpm --upgrade {{path/to/package.rpm}} --force`

- 确定文件的所有者并显示该包的版本：

`rpm --query --file {{/etc/postfix/main.cf}}`

- 列出包拥有的文件：

`rpm --query --list {{kernel}}`

- 显示 RPM 文件中的脚本：

`rpm --query --package --scripts {{package.rpm}}`

- 显示匹配包的更改、缺失和/或安装不正确的文件：

`rpm --verify --all '{{php-*}}'`

- 显示特定包的变更日志：

`rpm --query --changelog {{package}}`