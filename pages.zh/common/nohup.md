# nohup

> 允许进程在终端关闭后继续运行。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>。

- 运行一个可在终端关闭后继续运行的进程：

`nohup {{命令}} {{参数1 参数2 ...}}`

- 在后台模式下启动 `nohup`：

`nohup {{命令}} {{参数1 参数2 ...}} &`

- 运行一个可在终端关闭后继续运行的 shell 脚本：

`nohup {{路径/到/脚本.sh}} &`

- 运行一个进程，并将输出写入指定文件：

`nohup {{命令}} {{参数1 参数2 ...}} > {{路径/到/输出文件}} &`
