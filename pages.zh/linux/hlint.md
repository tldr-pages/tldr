# hlint

> 建议改进 Haskell 代码。
> 更多信息：<https://hackage.haskell.org/package/hlint>.

- 显示给定文件的改进建议：

`hlint {{path/to/file}} options`

- 检查所有 Haskell 文件并生成报告：

`hlint {{path/to/directory}} --report`

- 自动应用大部分建议：

`hlint {{path/to/file}} --refactor`

- 显示更多选项：

`hlint {{path/to/file}} --refactor-options`

- 生成忽略所有现有提示的设置文件：

`hlint {{path/to/file}} --default > {{.hlint.yaml}}`