# 选择

> Bash 内置构造，用于创建菜单。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-select>。

- 从单个单词创建菜单：

`select {{word}} in {{苹果 橙子 梨子 香蕉}}; do echo ${{word}}; done`

- 从另一个命令的输出创建菜单：

`select {{line}} in $({{命令}}); do echo ${{line}}; done`

- 为 `select` 指定提示字符串，并从当前目录中选择文件或文件夹创建菜单：

`PS3="{{选择一个文件: }}"; select {{file}} in *; do echo ${{file}}; done`

- 从 Bash 数组创建菜单：

`{{fruits}}=({{苹果 橙子 梨子 香蕉}}); select {{word}} in ${{{fruits[@]}}}; do echo ${{word}}; done`