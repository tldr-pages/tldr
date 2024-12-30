# 暂停

> 暂停当前 shell 的执行。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-suspend>。

- 暂停当前 shell（在嵌套 shell 中如 `su` 时非常有用）：

`{{bash}} <Enter> suspend`

- 如果在非嵌套 shell 中使用了 `suspend`，可以在单独的终端中继续执行：

`pkill -CONT bash`

- 强制暂停，即使这会使你无法访问系统：

`suspend -f`