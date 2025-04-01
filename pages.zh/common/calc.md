# calc

> 终端中的交互式任意精度计算器。
> 更多信息：<https://manned.org/calc>.

- 以交互模式启动 `calc`：

`calc`

- 在非交互模式下进行计算：

`calc '{{85 * (36 / 4)}}'`

- 不格式化输出（用于管道）：

`calc -p '{{4/3 * pi() * 5^3}}'`

- 进行计算后切换到交互模式：

`calc -i '{{sqrt(2)}}'`

- 以特定权限模式启动 `calc`（0 到 7，默认为 7）：

`calc -m {{mode}}`

- 查看 `calc` 的简介：

`calc help intro`

- 查看 `calc` 的概述：

`calc help overview`

- 打开 `calc` 手册：

`calc help`
