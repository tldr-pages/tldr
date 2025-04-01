# suspend

> 暂停当前 shell 的执行。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-suspend>.

- 暂停当前 shell（在嵌套 shell 如 `su` 中时非常有用）：

`{{bash}} <Enter> suspend`

- 如果在非嵌套 shell 中使用了 `suspend`，则从暂停状态恢复（在另一个终端中运行此命令）：

`pkill -CONT bash`

- 即使这会导致你无法登录系统，也强制暂停：

`suspend -f`
