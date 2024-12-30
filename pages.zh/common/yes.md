# 是的

> 重复输出某些内容。
> 此命令通常用于对安装命令（如 apt-get）的每个提示回答“是”。
> 更多信息：<https://www.gnu.org/software/coreutils/yes>。

- 重复输出“消息”：

`yes {{消息}}`

- 重复输出“y”：

`yes`

- 接受 `apt-get` 命令提示的所有内容：

`yes | sudo apt-get install {{程序}}`

- 重复输出换行符，以始终接受提示的默认选项：

`yes ''`