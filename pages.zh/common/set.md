# set

> 切换 shell 选项或设置定位参数的值。
> 更多信息：<https://manned.org/set.1posix>.

- 显示 shell 变量的名称及其值：

`set`

- 将新初始化的变量导出到子进程中：

`set -a`

- 当作业完成时，向 `stderr` 写入格式化的消息：

`set -b`

- 用类似 `vi` 的键绑定（例如 `yy`）在命令行中写入和编辑文本：

`set -o {{vi}}`

- 返回默认模式：

`set -o {{emacs}}`

- 列出所有模式：

`set -o`

- 当（某些）命令失败时退出 shell：

`set -e`

- 重置所有 shell 参数并分配新的参数：

`set -- {{argument1 argument2 ...}}`
