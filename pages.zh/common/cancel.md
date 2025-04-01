# cancel

> 取消打印任务。
> 参见：`lp`, `lpmove`, `lpstat`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-cancel.html>。

- 取消默认打印机（使用 `lpoptions -d {{printer}}` 设置）的当前任务：

`cancel`

- 取消特定 [u]ser 拥有的默认打印机的所有任务：

`cancel -u {{username}}`

- 取消特定打印机的当前任务：

`cancel {{printer}}`

- 取消特定打印机上的特定任务：

`cancel {{printer}}-{{job_id}}`

- 取消所有打印机的所有任务：

`cancel -a`

- 取消特定打印机的所有任务：

`cancel -a {{printer}}`

- 取消特定服务器的当前任务并删除 ([x]) 任务数据文件：

`cancel -h {{server}} -x`
