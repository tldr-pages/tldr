# yes

> 重复输出指定的字符串。
> 此命令通常用于自动回答安装命令（如 `apt-get`）的所有提示。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>。

- 重复输出 `y`：

`yes`

- 重复输出指定的值：

`yes {{值}}`

- 自动接受 `apt-get` 命令的所有提示：

`yes | sudo apt-get install {{程序}}`

- 重复输出空行，始终接受提示的默认选项：

`yes ''`
