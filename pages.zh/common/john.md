# john

> 密码破解工具。
> 更多信息：<https://www.openwall.com/john/>.

- 破解密码哈希：

`john {{路径/到/hashes.txt}}`

- 显示已破解的密码：

`john --show {{路径/到/hashes.txt}}`

- 按用户标识符从多个文件中显示用户的已破解密码：

`john --show --users={{用户_IDs}} {{路径/到/hashes1.txt 路径/到/hashes2.txt ...}}`

- 使用自定义的单词列表破解密码哈希：

`john --wordlist={{路径/到/wordlist.txt}} {{路径/到/hashes.txt}}`

- 列出可用的哈希格式：

`john --list=formats`

- 使用特定的哈希格式破解密码哈希：

`john --format={{md5crypt}} {{路径/到/hashes.txt}}`

- 启用单词变形规则破解密码哈希：

`john --rules {{路径/到/hashes.txt}}`

- 从状态文件恢复一个中断的破解会话，例如：`mycrack.rec`：

`john --restore={{路径/到/mycrack.rec}}`
