# disown

> 允许子进程在它们所附加的 shell 之外继续存在。
> 另见 `jobs` 命令。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-disown>。

- 解除当前作业的关联：

`disown`

- 解除特定作业的关联：

`disown %{{job_number}}`

- 解除所有作业的关联：

`disown -a`

- 保持作业（不解除关联），但标记它以便在 shell 退出时不会接收到未来的 SIGHUP：

`disown -h %{{job_number}}`