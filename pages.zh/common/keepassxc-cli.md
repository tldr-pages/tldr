# keepassxc-cli

> KeepassXC 的命令行接口。
> 更多信息：<https://manned.org/keepassxc-cli>.

- 搜索条目：

`keepassxc-cli search {{path/to/database_file}} {{name}}`

- 列出文件夹的内容：

`keepassxc-cli ls {{path/to/database_file}} {{/path/to/directory}}`

- 添加一个带有自动生成密码的条目：

`keepassxc-cli add --generate {{path/to/database_file}} {{entry_name}}`

- 删除一个条目：

`keepassxc-cli rm {{path/to/database_file}} {{entry_name}}`

- 将条目的密码复制到剪贴板：

`keepassxc-cli clip {{path/to/database_file}} {{entry_name}}`

- 将 TOTP 代码复制到剪贴板：

`keepassxc-cli clip --totp {{path/to/database_file}} {{entry_name}}`

- 生成一个包含 7 个单词的密码短语：

`keepassxc-cli diceware --words {{7}}`

- 生成一个包含 16 个可打印 ASCII 字符的密码：

`keepassxc-cli generate --lower --upper --numeric --special --length {{16}}`