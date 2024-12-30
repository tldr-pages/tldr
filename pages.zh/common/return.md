# 返回

> 如果通过 `source` 运行，则退出一个函数或脚本。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-return>。

- 提前退出一个函数：

`{{func_name}}() { {{echo "这被执行到了"}}; return; {{echo "这不会被执行"}}; }`

- 指定函数的返回值：

`{{func_name}}() { return {{N}}; }`