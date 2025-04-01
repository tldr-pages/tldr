# guile

> Guile Scheme 解释器。
> 更多信息：<https://www.gnu.org/software/guile>.

- 启动 REPL（交互式 shell）：

`guile`

- 执行给定 Scheme 文件中的脚本：

`guile {{script.scm}}`

- 执行 Scheme 表达式：

`guile -c "{{expression}}"`

- 在指定的端口或 Unix 域套接字（默认端口为 37146）上监听远程 REPL 连接：

`guile --listen={{port_or_socket}}`
