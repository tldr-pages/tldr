# yes

> 重复输出某些内容。
> 此命令通常用于对安装命令（如 `apt-get`）每个提示回答是。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- 重复输出“{{消息}}”：

`yes {{消息}}`

- 重复输出“y”：

`yes`

- 接受 `apt-get` 命令的所有提示：

`yes | sudo apt-get install {{程序}}`

- 重复输出一个换行符以始终接受提示的默认选项：

`yes ''`
