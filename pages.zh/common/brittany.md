# brittany

> 美化 Haskell 源文件。
> 更多信息：<https://github.com/lspitzner/brittany#readme>。

- 格式化 Haskell 源文件并将结果打印到 `stdout`：

`brittany {{path/to/file.hs}}`

- 在当前目录中就地格式化所有 Haskell 源文件：

`brittany --write-mode=inplace {{*.hs}}`

- 检查 Haskell 源文件是否需要更改，并通过程序的退出代码指示结果：

`brittany --check-mode {{path/to/file.hs}}`

- 使用指定的缩进级别空格数和行长度格式化 Haskell 源文件：

`brittany --indent {{4}} --columns {{100}} {{path/to/file.hs}}`

- 根据指定配置文件中定义的样式格式化 Haskell 源文件：

`brittany --config-file {{path/to/config.yaml}} {{path/to/file.hs}}`