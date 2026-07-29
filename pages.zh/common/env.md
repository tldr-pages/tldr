# env

> 显示环境变量或在修改后的环境中运行程序。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>。

- 显示环境变量：

`env`

- 运行程序。常用于脚本中的 shebang（`#!`）之后，用于查找程序的路径：

`env {{程序}}`

- 清空环境并运行程序：

`env {{[-i|--ignore-environment]}} {{程序}}`

- 从环境中移除变量并运行程序：

`env {{[-u|--unset]}} {{变量名}} {{程序}}`

- 设置变量并运行程序：

`env {{变量名}}={{值}} {{程序}}`

- 设置一个或多个变量并运行程序：

`env {{变量1=值 变量2=值 变量3=值 ...}} {{程序}}`

- 以不同的名称运行程序：

`env {{[-a|--argv0]}} {{自定义名称}} {{程序}}`
