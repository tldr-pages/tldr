# xkcdpass

> 一个灵活且可脚本化的密码生成器，可以生成强大的短语密码。
> 受 XKCD 936 启发。
> 更多信息：<https://github.com/redacted/XKCD-password-generator>.

- 使用默认选项生成一个短语密码：

`xkcdpass`

- 生成一个短语密码，其每个单词的首字母匹配提供的参数：

`xkcdpass -a {{acrostic}}`

- 交互式生成密码：

`xkcdpass -i`