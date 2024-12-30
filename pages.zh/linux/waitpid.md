# waitpid

> 等待任意进程的终止。
> 另见：`wait`。
> 更多信息：<https://manned.org/waitpid.1>。

- 睡眠直到所有指定 PID 的进程已退出：

`waitpid {{pid1 pid2 ...}}`

- 最多睡眠 `n` 秒：

`waitpid --timeout {{n}} {{pid1 pid2 ...}}`

- 如果指定的 PID 已经退出，则不报错：

`waitpid --exited {{pid1 pid2 ...}}`

- 睡眠直到指定的 `n` 个进程已退出：

`waitpid --count {{n}} {{pid1 pid2 ...}}`

- 显示帮助：

`waitpid -h`