# fcrackzip

> ZIP档案密码破解工具。
> 更多信息：<https://manned.org/fcrackzip>。

- 使用暴力破解一个长度为4到8个字符的密码，并且只包含字母数字字符（顺序很重要）：

`fcrackzip --brute-force --length 4-8 --charset aA1 {{archive}}`

- 在详细模式下暴力破解一个长度为3个字符的密码，只包含小写字母、`$`和`%`：

`fcrackzip -v --brute-force --length 3 --charset a:$% {{archive}}`

- 暴力破解一个只包含小写字母和特殊字符的密码：

`fcrackzip --brute-force --length 4 --charset a! {{archive}}`

- 从密码`12345`开始暴力破解一个只包含数字的密码：

`fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 {{archive}}`

- 使用字典破解密码：

`fcrackzip --use-unzip --dictionary --init-password {{wordlist}} {{archive}}`

- 基准测试破解性能：

`fcrackzip --benchmark`