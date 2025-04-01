# return

> 退出函数或脚本（如果使用 `source` 运行）。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-return>.

- 提前退出函数：

`{{func_name}}() { {{echo "这里会被执行"}}; return; {{echo "这里不会被执行"}}; }`

- 指定函数的返回值：

`{{func_name}}() { return {{exit_code}}; }`