# ghci

> Glasgow Haskell 编译器的交互环境。
> 更多信息：<https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>。

- 启动 REPL（交互 shell）：

`ghci`

- 启动 REPL 并加载指定的 Haskell 源文件：

`ghci {{source_file.hs}}`

- 启动 REPL 并启用语言选项：

`ghci -X{{language_option}}`

- 启动 REPL 并启用某些级别的编译器警告（例如 `all` 或 `compact`）：

`ghci -W{{warning_level}}`

- 启动 REPL 并使用冒号分隔的目录列表来查找源文件：

`ghci -i{{path/to/directory1:path/to/directory2:...}}`