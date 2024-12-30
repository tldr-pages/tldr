# bc

> 一个任意精度计算器语言。
> 另见：`dc`，`qalc`。
> 更多信息：<https://manned.org/bc>。

- 开始一个交互式会话：

`bc`

- 启动一个启用标准数学库的 [i]nteractive 会话 [l]ibrary：

`bc --interactive --mathlib`

- 计算一个表达式：

`echo '{{5 / 3}}' | bc`

- 执行一个脚本：

`bc {{path/to/script.bc}}`

- 计算一个具有指定小数位数的表达式：

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- 使用 `mathlib` 计算正弦/余弦/反正切/自然对数/指数函数：

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`

- 执行一个内联阶乘脚本：

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`