# set

> 切换 shell 选项或设置位置参数的值。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#The-Set-Builtin>。

- 显示 shell 变量的名称和值：

`set`

- 将新初始化的变量导出到子进程：

`set -a`

- 作业完成时将格式化消息写入 `stderr`：

`set -b`

- 使用类似 `vi` 的键绑定在命令行中编写和编辑文本（如 `yy`）：

`set -o vi`

- 返回默认（`emacs`）模式：

`set -o emacs`

- 列出所有模式：

`set -o`

- 当（某些）命令失败时退出 shell：

`set -e`

- 重置所有 shell 参数并分配新参数：

`set -- {{参数1 参数2 ...}}`
