# continue

> 跳到 `for`、`while`、`until` 或 `select` 循环的下一次迭代。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-continue>.

- 跳到循环的下一次迭代：

`while :; do continue; echo "此行永远不会被执行"; done`

- 从嵌套循环中跳到外层循环的下一次迭代：

`for i in {1..3}; do while :; do continue 2; done; done`
