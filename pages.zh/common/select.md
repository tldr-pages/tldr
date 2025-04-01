# select

> Bash 内置命令，用于创建菜单。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-select>.

- 使用单独的单词创建菜单：

`select {{word}} in {{apple orange pear banana}}; do echo ${{word}}; done`

- 从其他命令的输出创建菜单：

`select {{line}} in $({{command}}); do echo ${{line}}; done`

- 指定 `select` 的提示字符串，并创建一个从当前目录中选择文件或文件夹的菜单：

`PS3="{{选择一个文件: }}"; select {{file}} in *; do echo ${{file}}; done`

- 从 Bash 数组创建菜单：

`{{fruits}}=({{apple orange pear banana}}); select {{word}} in ${{{fruits[@]}}}; do echo ${{word}}; done`