# fcrackzip

> ZIP 存档密码破解工具。
> 更多信息：<https://manned.org/fcrackzip>。

- 对长度为 4 到 8 个字符、只包含字母数字字符的密码进行暴力破解（顺序重要）：

`fcrackzip --brute-force --length 4-8 --charset aA1 {{archive}}`

- 在详细模式下对长度为 3 个字符、只包含小写字母、`$` 和 `%` 的密码进行暴力破解：

`fcrackzip -v --brute-force --length 3 --charset a:$% {{archive}}`

- 对只包含小写和特殊字符的密码进行暴力破解：

`fcrackzip --brute-force --length 4 --charset a! {{archive}}`

- 对只包含数字的密码进行暴力破解，从密码 `12345` 开始：

`fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 {{archive}}`

- 使用字典破解密码：

`fcrackzip --use-unzip --dictionary --init-password {{wordlist}} {{archive}}`

- 测试破解性能：

`fcrackzip --benchmark`