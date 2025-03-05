# print

> Z Shell (`zsh`) 内置。打印参数，类似于 `echo`。
> 另请参阅：`echo`、`printf`、`zsh`。
> 更多信息：<https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- 打印输入：

`print "文本1" "文本2"`

- 以换行符分隔打印：

`print -l "第一行" "第二行" "第三行"`

- 不带尾随换行符打印：

`print -n "文本"; print "文本2"`

- 启用反斜杠转义：

`print -e "第一行\n第二行"`

- 按照 `printf` 所述打印参数（为了在 shell 之间实现更好的可移植性，请考虑改用 `printf` 命令）：

`print -f "%s 今年 %d 岁了。\n" "小明" 30`
