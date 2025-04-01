# navi

> 一个用于命令行和应用程序启动器的交互式速查工具。
> 更多信息：<https://github.com/denisidoro/navi>.

- 浏览所有可用的速查表：

`navi`

- 浏览 `navi` 自身的速查表：

`navi fn welcome`

- 从速查表中打印命令但不执行：

`navi --print`

- 输出 shell 小部件源代码（如果可能，它会自动检测你的 shell，也可以手动指定）：

`navi widget {{shell}}`

- 自动选择并执行与查询最匹配的代码段：

`navi --query '{{query}}' --best-match`