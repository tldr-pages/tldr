# nohup

> 允许进程在终端被杀死后继续运行。
> 更多信息：<https://www.gnu.org/software/coreutils/nohup>。

- 运行一个可以在终端之外继续运行的进程：

`nohup {{command}} {{argument1 argument2 ...}}`

- 以后台模式启动 `nohup`：

`nohup {{command}} {{argument1 argument2 ...}} &`

- 运行一个可以在终端之外继续运行的 shell 脚本：

`nohup {{path/to/script.sh}} &`

- 运行一个进程并将输出写入特定文件：

`nohup {{command}} {{argument1 argument2 ...}} > {{path/to/output_file}} &`