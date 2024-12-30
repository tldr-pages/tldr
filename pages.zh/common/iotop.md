# iotop

> 显示当前进程或线程的 I/O 使用情况表。
> 更多信息请访问: <https://manned.org/iotop>。

- 启动类似 top 的 I/O 监视器：

`sudo iotop`

- 仅显示实际进行 I/O 的进程或线程：

`sudo iotop --only`

- 以非交互模式显示 I/O 使用情况：

`sudo iotop --batch`

- 仅显示进程的 I/O 使用情况（默认显示所有线程）：

`sudo iotop --processes`

- 显示特定 PID 的 I/O 使用情况：

`sudo iotop --pid={{PID}}`

- 显示特定用户的 I/O 使用情况：

`sudo iotop --user={{user}}`

- 显示累计 I/O 而不是带宽：

`sudo iotop --accumulated`