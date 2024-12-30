# 重试

> 重复命令直到成功或满足某个条件。
> 更多信息：<https://github.com/minfrin/retry>。

- 重试一个命令直到成功：

`retry {{command}}`

- 每隔 n 秒重试一个命令直到成功：

`retry --delay={{n}} {{command}}`

- 在 n 次尝试后放弃：

`retry --times={{n}} {{command}}`