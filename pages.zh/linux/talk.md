# talk

> 一个可视通信程序，可以将您终端的内容复制到另一个用户的终端。
> 更多信息：<https://www.gnu.org/software/inetutils/manual/html_node/talk-invocation.html>.

- 与同一机器上的用户开始 talk 会话：

`talk {{username}}`

- 与同一机器上登录到 tty3 的用户开始 talk 会话：

`talk {{username}} {{tty3}}`

- 与远程机器上的用户开始 talk 会话：

`talk {{username}}@{{hostname}}`

- 清除两个终端屏幕上的文本：

`<Ctrl d>`

- 退出 talk 会话：

`<Ctrl c>`
