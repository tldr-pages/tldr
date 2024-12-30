# keepassxc-cli

> KeepassXC 的命令行界面。
> 更多信息：<https://manned.org/keepassxc-cli>。

- 搜索条目：

`keepassxc-cli search {{数据库文件路径}} {{名称}}`

- 列出文件夹的内容：

`keepassxc-cli ls {{数据库文件路径}} {{/文件夹路径}}`

- 添加一个带有自动生成密码的条目：

`keepassxc-cli add --generate {{数据库文件路径}} {{条目名称}}`

- 删除一个条目：

`keepassxc-cli rm {{数据库文件路径}} {{条目名称}}`

- 将条目的密码复制到剪贴板：

`keepassxc-cli clip {{数据库文件路径}} {{条目名称}}`

- 将 TOTP 代码复制到剪贴板：

`keepassxc-cli clip --totp {{数据库文件路径}} {{条目名称}}`

- 生成一个包含 7 个单词的密码短语：

`keepassxc-cli diceware --words {{7}}`

- 生成一个包含 16 个可打印 ASCII 字符的密码：

`keepassxc-cli generate --lower --upper --numeric --special --length {{16}}`