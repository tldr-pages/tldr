# hlint

> 提供对 Haskell 代码的改进建议。
> 更多信息请访问：<https://hackage.haskell.org/package/hlint>。

- 显示给定文件的建议：

`hlint {{path/to/file}} options`

- 检查所有 Haskell 文件并生成报告：

`hlint {{path/to/directory}} --report`

- 自动应用大多数建议：

`hlint {{path/to/file}} --refactor`

- 显示额外选项：

`hlint {{path/to/file}} --refactor-options`

- 生成一个忽略所有未解决提示的设置文件：

`hlint {{path/to/file}} --default > {{.hlint.yaml}}`