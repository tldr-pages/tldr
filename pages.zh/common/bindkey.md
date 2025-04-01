# bindkey

> 为 Z-Shell 添加快捷键绑定。
> 更多信息：<https://zsh.sourceforge.io/Guide/zshguide04.html>。

- 将快捷键绑定到特定命令：

`bindkey "{{^k}}" {{kill-line}}`

- 将快捷键绑定到特定键 [s]序列：

`bindkey -s '^o' 'cd ..\n'`

- [l]列出键映射：

`bindkey -l`

- 查看键[M]映射中的快捷键：

`bindkey -M main`
