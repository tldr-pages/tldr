# navi

> 一个用于命令行和应用程序启动器的互动备忘单工具。
> 更多信息：<https://github.com/denisidoro/navi>。

- 浏览所有可用的备忘单：

`navi`

- 浏览 `navi` 本身的备忘单：

`navi fn welcome`

- 从备忘单中打印一个命令而不执行它：

`navi --print`

- 输出 shell 小部件源代码（如果可能，它会自动检测你的 shell，但也可以手动指定）：

`navi widget {{shell}}`

- 自动选择并执行最符合查询的代码片段：

`navi --query '{{query}}' --best-match`