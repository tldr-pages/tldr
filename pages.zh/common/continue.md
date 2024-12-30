# 继续

> 跳过 `for`、`while`、`until` 或 `select` 循环的下一次迭代。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-continue>。

- 跳过下一次迭代：

`while :; do continue; echo "这将永远无法到达"; done`

- 从嵌套循环中跳过下一次迭代：

`for i in {1..3}; do while :; do continue 2; done; done`