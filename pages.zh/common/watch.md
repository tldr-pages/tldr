# watch

> 定期执行程序并全屏监控输出。
> 更多信息：<https://manned.org/watch>。

- 重复运行命令并显示结果：

`watch {{命令}}`

- 每 60 秒重新运行一次命令：

`watch {{[-n|--interval]}} 60 {{命令}}`

- 监控磁盘空间，高亮显示变化：

`watch {{[-d|--differences]}} df`

- 重复运行管道并显示结果：

`watch "{{命令1}} | {{命令2}} | {{命令3}}"`

- 如果可见输出发生变化则退出 `watch`：

`watch {{[-g|--chgexit]}} {{lsblk}}`

- 解释终端控制字符：

`watch {{[-c|--color]}} {{ls --color=always}}`
