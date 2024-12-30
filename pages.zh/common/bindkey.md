# bindkey

> 为 Z-Shell 添加键绑定。
> 更多信息：<https://zsh.sourceforge.io/Guide/zshguide04.html>。

- 将热键绑定到特定命令：

`bindkey "{{^k}}" {{kill-line}}`

- 将热键绑定到特定键 [s]equence：

`bindkey -s '^o' 'cd ..\n'`

- [l]ist 键映射：

`bindkey -l`

- 在键 [M]ap 中查看热键：

`bindkey -M main`