# return

> 退出函数。
> 如果使用 `source` 运行，可以退出脚本。
> 另请参阅：`exit`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-return>。

- 提前退出函数：

`{{函数名}}() { {{echo "这会执行"}}; return; {{echo "这不会执行"}}; }`

- 指定函数的返回值：

`{{函数名}}() { return {{退出码}}; }`
