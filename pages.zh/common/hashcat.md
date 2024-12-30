# hashcat

> 快速而先进的密码恢复工具。
> 更多信息请访问：<https://hashcat.net/wiki/doku.php?id=hashcat>。

- 使用默认的 hashcat 掩码进行暴力攻击（模式 3）：

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} {{hash_value}}`

- 使用已知的 4 位数字模式进行暴力攻击（模式 3）：

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} {{hash_value}} "{{?d?d?d?d}}"`

- 使用最多 8 个可打印的 ASCII 字符进行暴力攻击（模式 3）：

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} --increment {{hash_value}} "{{?a?a?a?a?a?a?a?a}}"`

- 使用 Kali Linux 盒子中的 RockYou 字典进行字典攻击（模式 0）：

`hashcat --hash-type {{hash_type_id}} --attack-mode {{0}} {{hash_value}} {{/usr/share/wordlists/rockyou.txt}}`

- 使用经过常见密码变体变异的 RockYou 字典进行基于规则的字典攻击（模式 0）：

`hashcat --hash-type {{hash_type_id}} --attack-mode {{0}} --rules-file {{/usr/share/hashcat/rules/best64.rule}} {{hash_value}} {{/usr/share/wordlists/rockyou.txt}}`

- 使用来自两个不同自定义字典的单词串联进行组合攻击（模式 1）：

`hashcat --hash-type {{hash_type_id}} --attack-mode {{1}} {{hash_value}} {{/path/to/dictionary1.txt}} {{/path/to/dictionary2.txt}}`

- 显示已破解哈希的结果：

`hashcat --show {{hash_value}}`

- 显示所有示例哈希：

`hashcat --example-hashes`