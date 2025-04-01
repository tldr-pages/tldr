# dlv

> Go 编程语言的调试器。
> 更多信息：<https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md>.

- 编译并开始调试当前目录中的主包（默认情况下，不带参数）：

`dlv debug`

- 编译并开始调试特定的包：

`dlv debug {{package}} {{arguments}}`

- 编译测试二进制文件并开始调试编译后的程序：

`dlv test`

- 连接到无头调试服务器：

`dlv connect {{ip_address}}`

- 附加到正在运行的进程并开始调试：

`dlv attach {{pid}}`

- 编译并开始跟踪程序：

`dlv trace {{package}} --regexp '{{regular_expression}}'`
