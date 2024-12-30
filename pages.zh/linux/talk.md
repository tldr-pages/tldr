# 通话

> 一款可视化通信程序，能够将你的终端中的信息复制到另一位用户的终端中。
> 更多信息：<https://www.gnu.org/software/inetutils/manual/html_node/talk-invocation.html>。

- 与同一台机器上的用户开始通话会话：

`talk {{用户名}}`

- 与同一台机器上登录在tty3的用户开始通话会话：

`talk {{用户名}} {{tty3}}`

- 与远程机器上的用户开始通话会话：

`talk {{用户名}}@{{主机名}}`

- 清除两个终端屏幕上的文本：

`<Ctrl>+D`

- 退出通话会话：

`<Ctrl>+C`