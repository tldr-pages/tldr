# break

> 跳出 `for`、`while`、`until` 或 `select` 循环。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-break>。

- 跳出单层循环：

`while :; do break; done`

- 跳出嵌套循环：

`while :; do while :; do break 2; done; done`
