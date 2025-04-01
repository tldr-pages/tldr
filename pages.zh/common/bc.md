# bc

> 任意精度的计算器语言。
> 请参阅：`dc`，`qalc`。
> 更多信息：<https://manned.org/bc>.

- 启动交互式会话：

`bc`

- 启动交互式会话并启用标准数学库：

`bc --interactive --mathlib`

- 计算表达式：

`echo '{{5 / 3}}' | bc`

- 执行脚本：

`bc {{路径/到/脚本.bc}}`

- 使用指定的小数位数计算一个表达式：

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- 使用 `mathlib` 计算正弦/余弦/反正切/自然对数/指数函数：

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`

- 执行一个内联的阶乘脚本：

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`
