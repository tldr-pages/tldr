# makepasswd

> 生成和加密密码。
> 更多信息：<https://manpages.debian.org/latest/makepasswd/makepasswd.1.en.html>.

- 生成一个随机密码（8 到 10 个字符，包含字母和数字）：

`makepasswd`

- 生成一个 10 个字符的密码：

`makepasswd --chars {{10}}`

- 生成一个 5 到 10 个字符的密码：

`makepasswd --minchars {{5}} --maxchars {{10}}`

- 生成一个只包含 "b"、"a" 或 "r" 字符的密码：

`makepasswd --string {{bar}}`
