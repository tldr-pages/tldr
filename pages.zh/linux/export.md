# 导出

> 将 shell 变量导出到子进程。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-export>。

- 设置环境变量：

`export {{VARIABLE}}={{value}}`

- 撤销环境变量：

`export -n {{VARIABLE}}`

- 将函数导出到子进程：

`export -f {{FUNCTION_NAME}}`

- 将路径附加到环境变量 `PATH`：

`export PATH=$PATH:{{path/to/append}}`

- 以 shell 命令形式显示活动导出变量的列表：

`export -p`