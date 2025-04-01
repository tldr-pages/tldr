# waitpid

> 等待任意进程终止。
> 参见：`wait`。
> 更多信息：<https://manned.org/waitpid.1>.

- 等待指定的进程ID对应的进程全部退出后继续：

`waitpid {{pid1 pid2 ...}}`

- 最多等待 `n` 秒：

`waitpid {{[-t|--timeout]}} {{n}} {{pid1 pid2 ...}}`

- 如果指定的进程ID已经退出，则不报错：

`waitpid {{[-e|--exited]}} {{pid1 pid2 ...}}`

- 等待直到指定的 `n` 个进程退出：

`waitpid {{[-c|--count]}} {{n}} {{pid1 pid2 ...}}`

- 显示帮助信息：

`waitpid {{[-h|--help]}}`
