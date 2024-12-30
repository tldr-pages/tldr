# Guile

> Guile Scheme 解释器。
> 更多信息：<https://www.gnu.org/software/guile>。

- 启动一个 REPL（交互式命令行）：

`guile`

- 执行给定 Scheme 文件中的脚本：

`guile {{script.scm}}`

- 执行一个 Scheme 表达式：

`guile -c "{{expression}}"`

- 监听一个端口或 Unix 域套接字（默认是 37146 端口）以进行远程 REPL 连接：

`guile --listen={{port_or_socket}}`