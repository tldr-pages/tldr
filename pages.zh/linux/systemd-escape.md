# systemd-escape

> 用于在systemd单元名称中使用的字符串转义。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-escape.html>。

- 转义给定文本：

`systemd-escape {{text}}`

- 反转转义过程：

`systemd-escape --unescape {{text}}`

- 将给定文本视为路径：

`systemd-escape --path {{text}}`

- 将给定后缀附加到转义文本：

`systemd-escape --suffix {{suffix}} {{text}}`

- 使用模板并注入转义文本：

`systemd-escape --template {{template}} {{text}}`