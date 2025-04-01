# export

> 将 shell 变量导出给子进程。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- 设置环境变量：

`export {{VARIABLE}}={{value}}`

- 取消设置环境变量：

`export -n {{VARIABLE}}`

- 将函数导出给子进程：

`export -f {{FUNCTION_NAME}}`

- 将路径名追加到环境变量 `PATH`：

`export PATH=$PATH:{{path/to/append}}`

- 以 shell 命令形式显示当前已导出的变量列表：

`export -p`
