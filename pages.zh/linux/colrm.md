# colrm

> 从 `stdin` 中删除列。
> 更多信息： <https://manned.org/colrm>。

- 删除 `stdin` 的第一列：

`colrm {{1 1}}`

- 从每行的第 3 列开始删除直到行尾：

`colrm {{3}}`

- 从每行的第 3 列删除到第 5 列：

`colrm {{3 5}}`