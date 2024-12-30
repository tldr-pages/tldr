# bc

> 一个任意精度计算器语言。
> 另见：`dc`。
> 更多信息：<https://keith.github.io/xcode-man-pages/bc.1.html>。

- 开始一个交互式会话：

`bc`

- 启用标准数学库开始一个交互式会话：

`bc --mathlib`

- 计算一个表达式：

`bc --expression='{{5 / 3}}'`

- 执行一个脚本：

`bc {{path/to/script.bc}}`

- 以指定的精度计算一个表达式：

`bc --expression='scale = {{10}}; {{5 / 3}}'`

- 使用 `mathlib` 计算正弦/余弦/反正切/自然对数/指数函数：

`bc --mathlib --expression='{{s|c|a|l|e}}({{1}})'`