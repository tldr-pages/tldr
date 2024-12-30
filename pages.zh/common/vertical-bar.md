# 垂直条

> 在程序之间传递数据。
> 更多信息：<https://gnu.org/software/bash/manual/bash.html#Pipelines>。

- 将 `stdout` 管道到 `stdin`：

`{{command}} | {{command}}`

- 将 `stdout` 和 `stderr` 都管道到 `stdin`：

`{{command}} |& {{command}}`