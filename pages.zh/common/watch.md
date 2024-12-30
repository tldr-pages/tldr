# watch

> 定期执行程序，并全屏显示输出。
> 更多信息：<https://manned.org/watch>。

- 重复运行命令并显示结果：

`watch {{command}}`

- 每60秒重新运行命令：

`watch -n {{60}} {{command}}`

- 监视目录内容，实时突出显示差异：

`watch -d {{ls -l}}`

- 重复运行管道并显示结果：

`watch '{{command_1}} | {{command_2}} | {{command_3}}'`