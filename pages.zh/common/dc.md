# dc

> 一个任意精度的计算器。使用逆波兰表示法（RPN）。
> 参见: `bc`, `qalc`。
> 更多信息: <https://www.gnu.org/software/bc/manual/dc-1.05/html_mono/dc.html>。

- 启动交互式会话:

`dc`

- 执行脚本:

`dc {{path/to/script.dc}}`

- 使用指定的精度计算表达式:

`dc {{[-e|--expression]}} '{{10}} k {{5 3 /}} p'`

- 计算 4 乘以 5 (4 5 *)，减去 17 (17 -)，并打印结果:

`dc {{[-e|--expression]}} '4 5 * 17 - p'`

- 设置小数点后位数为 7 (7 k)，计算 5 除以 -3 (5 _3 /)，并打印结果:

`dc {{[-e|--expression]}} '7 k 5 _3 / p'`

- 计算黄金比例，phi: 设置小数点后位数为 100 (100 k)，计算 5 的平方根 (5 v) 加 1 (1 +)，除以 2 (2 /)，并打印结果:

`dc {{[-e|--expression]}} '100 k 5 v 1 + 2 / p'`
