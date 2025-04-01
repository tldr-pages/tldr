# nohup

> 允许进程在终端被关闭后继续运行。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>.

- 运行一个能在终端关闭后继续运行的进程：

`nohup {{command}} {{argument1 argument2 ...}}`

- 在后台模式下启动 `nohup`：

`nohup {{command}} {{argument1 argument2 ...}} &`

- 运行一个在终端关闭后仍能继续运行的 shell 脚本：

`nohup {{path/to/script.sh}} &`

- 运行一个进程，并将输出写入指定文件：

`nohup {{command}} {{argument1 argument2 ...}} > {{path/to/output_file}} &`
