# 取消

> 取消打印任务。
> 另见： `lp`, `lpmove`, `lpstat`。
> 更多信息： <https://openprinting.github.io/cups/doc/man-cancel.html>。

- 取消默认打印机的当前任务（使用 `lpoptions -d {{printer}}` 设置）：

`cancel`

- 取消由特定 [u]ser 拥有的默认打印机的任务：

`cancel -u {{username}}`

- 取消特定打印机的当前任务：

`cancel {{printer}}`

- 取消特定打印机的特定任务：

`cancel {{printer}}-{{job_id}}`

- 取消所有打印机的 [a]ll 任务：

`cancel -a`

- 取消特定打印机的 [a]ll 任务：

`cancel -a {{printer}}`

- 取消特定服务器的当前任务并删除 ([x]) 任务数据文件：

`cancel -h {{server}} -x`