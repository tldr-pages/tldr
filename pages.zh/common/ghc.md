# ghc

> The Glasgow Haskell 编译器。
> 编译和链接 Haskell 源文件。
> 更多信息：<https://www.haskell.org/ghc>.

- 查找并编译当前目录中的所有模块：

`ghc Main`

- 编译单个文件：

`ghc {{path/to/file.hs}}`

- 使用额外优化编译：

`ghc -O {{path/to/file.hs}}`

- 在生成目标文件 (.o) 后停止编译：

`ghc -c {{path/to/file.hs}}`

- 启动 REPL（交互式 shell）：

`ghci`

- 评估单个表达式：

`ghc -e {{expression}}`