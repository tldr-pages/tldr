# env

> 显示环境或在修改后的环境中运行程序。
> 更多信息：<https://www.gnu.org/software/coreutils/env>。

- 显示环境：

`env`

- 运行一个程序。通常在脚本的 shebang (#!) 后使用，以查找程序的路径：

`env {{program}}`

- 清除环境并运行一个程序：

`env -i {{program}}`

- 从环境中移除变量并运行一个程序：

`env -u {{variable}} {{program}}`

- 设置一个变量并运行一个程序：

`env {{variable}}={{value}} {{program}}`

- 设置一个或多个变量并运行一个程序：

`env {{variable1}}={{value}} {{variable2}}={{value}} {{variable3}}={{value}} {{program}}`