# retry

> 重复执行命令，直到成功或满足某个条件。
> 更多信息：<https://github.com/minfrin/retry>.

- 重复执行命令，直到成功：

`retry {{command}}`

- 每隔 n 秒重复执行命令，直到成功：

`retry --delay={{n}} {{command}}`

- 尝试 n 次后放弃：

`retry --times={{n}} {{command}}`