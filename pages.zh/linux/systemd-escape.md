# systemd-escape

> 用于在 systemd 单元名称中转义字符串。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-escape.html>.

- 转义给定的文本：

`systemd-escape {{text}}`

- 反转转义过程：

`systemd-escape --unescape {{text}}`

- 将给定的文本视为路径：

`systemd-escape --path {{text}}`

- 将给定的后缀附加到转义后的文本：

`systemd-escape --suffix {{suffix}} {{text}}`

- 使用模板并注入转义后的文本：

`systemd-escape --template {{template}} {{text}}`