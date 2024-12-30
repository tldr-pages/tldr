# yacas

> 又一个计算机代数系统。
> 更多信息: <https://www.yacas.org>。

- 开始一个交互式 `yacas` 会话：

`yacas`

- 在 `yacas` 会话中，执行一个语句：

`{{Integrate(x)Cos(x)}};`

- 在 `yacas` 会话中，显示一个示例：

`{{Example()}};`

- 退出 `yacas` 会话：

`{{quit}}`

- 执行一个或多个 `yacas` 脚本（不带终端或提示），然后退出：

`yacas -p -c {{path/to/script1}} {{path/to/script2}}`

- 执行并打印一个语句的结果，然后退出：

`echo "{{Echo( Deriv(x)Cos(1/x) );}}" | yacas -p -c /dev/stdin`