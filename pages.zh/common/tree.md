# tree

> 显示当前目录的内容，以树形结构展示。
> 更多信息：<https://manned.org/tree>。

- 打印文件和目录，深度限制为 'num' 层（其中 1 表示当前目录）：

`tree -L {{num}}`

- 仅打印目录：

`tree -d`

- 也打印隐藏文件，并启用颜色化：

`tree -a -C`

- 打印树形结构时不显示缩进线，而是显示完整路径（使用 `-N` 选项可以不转义不可打印字符）：

`tree -i -f`

- 打印每个文件的大小和每个目录的累计大小，以人类可读的格式显示：

`tree -s -h --du`

- 在树形层级中打印符合通配符（glob）模式的文件，同时剪枝掉不包含匹配文件的目录：

`tree -P '{{*.txt}}' --prune`

- 在树形层级中打印符合通配符（glob）模式的目录，同时剪枝掉不是所需目录的祖先目录：

`tree -P {{directory_name}} --matchdirs --prune`

- 打印树形结构时忽略指定的目录：

`tree -I '{{directory_name1|directory_name2}}'`