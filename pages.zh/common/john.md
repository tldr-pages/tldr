# john

> 密码破解工具。
> 更多信息：<https://www.openwall.com/john/>.

- 破解密码哈希：

`john {{路径/到/哈希.txt}}`

- 显示已破解的密码：

`john --show {{路径/到/哈希.txt}}`

- 按用户标识从多个文件显示用户的已破解密码：

`john --show --users={{用户_id}} {{路径/到/哈希1.txt 路径/到/哈希2.txt ...}}`

- 使用自定义字典破解密码哈希：

`john --wordlist={{路径/到/字典.txt}} {{路径/到/哈希.txt}}`

- 列出可用的哈希格式：

`john --list=formats`

- 使用特定哈希格式破解密码哈希：

`john --format={{md5crypt}} {{路径/到/哈希.txt}}`

- 破解密码哈希，启用词语变形规则：

`john --rules {{路径/到/哈希.txt}}`

- 从状态文件恢复一个中断的破解会话，例如 `mycrack.rec`：

`john --restore={{路径/到/mycrack.rec}}`