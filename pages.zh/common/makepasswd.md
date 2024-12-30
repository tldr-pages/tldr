# makepasswd

> 生成和加密密码。
> 更多信息: <https://manpages.debian.org/latest/makepasswd/makepasswd.1.en.html>。

- 生成一个随机密码（长度为8到10个字符，包含字母和数字）：

`makepasswd`

- 生成一个10个字符长的密码：

`makepasswd --chars {{10}}`

- 生成一个5到10个字符长的密码：

`makepasswd --minchars {{5}} --maxchars {{10}}`

- 生成一个仅包含字符“b”、“a”或“r”的密码：

`makepasswd --string {{bar}}`