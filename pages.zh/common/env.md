# env

> 显示环境变量或在修改后的环境中运行程序。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- 显示环境变量：

`env`

- 运行程序。通常在脚本中的 shebang (#!) 之后用于查找程序路径：

`env {{program}}`

- 清除环境变量并运行程序：

`env {{[-i|--ignore-environment]}} {{program}}`

- 从环境中移除变量并运行程序：

`env {{[-u|--unset]}} {{variable}} {{program}}`

- 设置变量并运行程序：

`env {{variable}}={{value}} {{program}}`

- 设置一个或多个变量并运行程序：

`env {{variable1}}={{value}} {{variable2}}={{value}} {{variable3}}={{value}} {{program}}`