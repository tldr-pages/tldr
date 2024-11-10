# hashcat

> 快速且先进的密码恢复工具。
> 更多信息：<https://hashcat.net/wiki/doku.php?id=hashcat>.

- 使用默认的 hashcat 掩码执行暴力破解攻击（模式 3）：

`hashcat --hash-type {{哈希类型id}} --attack-mode {{3}} {{哈希值}}`

- 使用已知的 4 位数字模式执行暴力破解攻击（模式 3）：

`hashcat --hash-type {{哈希类型id}} --attack-mode {{3}} {{哈希值}} "{{?d?d?d?d}}"`

- 使用最多 8 个可打印的 ASCII 字符执行暴力破解攻击（模式 3）：

`hashcat --hash-type {{哈希类型id}} --attack-mode {{3}} --increment {{哈希值}} "{{?a?a?a?a?a?a?a?a}}"`

- 使用 Kali Linux 系统中的 RockYou 字典执行字典攻击（模式 0）：

`hashcat --hash-type {{哈希类型id}} --attack-mode {{0}} {{哈希值}} {{/usr/share/wordlists/rockyou.txt}}`

- 使用经过常见密码变体规则变换的 RockYou 字典，执行字典攻击（模式 0）：

`hashcat --hash-type {{哈希类型id}} --attack-mode {{0}} --rules-file {{/usr/share/hashcat/rules/best64.rule}} {{哈希值}} {{/usr/share/wordlists/rockyou.txt}}`

- 连接两个不同自定义字典的单词并执行组合攻击（模式 1）：

`hashcat --hash-type {{哈希类型id}} --attack-mode {{1}} {{哈希值}} {{/路径/到/字典.txt}} {{/路径/到/字典.txt}}`

- 显示已经破解的哈希值的结果：

`hashcat --show {{哈希值}}`

- 显示所有示例哈希值：

`hashcat --example-hashes`
