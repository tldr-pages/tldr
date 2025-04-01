# watch

> 周期性地执行一个程序，并以全屏模式监控输出。
> 更多信息：<https://manned.org/watch>.

- 重复运行一个命令并显示结果：

`watch {{command}}`

- 每60秒重新运行一次命令：

`watch {{[-n|--interval]}} {{60}} {{command}}`

- 监控磁盘空间，高亮显示差异：

`watch {{[-d|--differences]}} {{df}}`

- 重复运行一个命令管道并显示结果：

`watch "{{command_1}} | {{command_2}} | {{command_3}}"`

- 如果可见输出发生变化，则退出 `watch`：

`watch {{[-g|--chgexit]}} {{lsblk}}`

- 解释终端控制字符：

`watch {{[-c|--color]}} {{ls --color=always}}`