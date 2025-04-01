# ghcid

> 用于 Haskell 的简单高效的命令行 IDE，文件更改时自动重新加载代码。
> 持续显示编译错误、警告和测试结果。
> 更多信息：<https://github.com/ndmitchell/ghcid>.

- 启动 `ghcid` 并监视 Haskell 文件的变化：

`ghcid {{path/to/Main.hs}}`

- 使用特定命令启动 `ghcid`，例如加载 Stack 或 Cabal 项目：

`ghcid --command "{{stack ghci Main.hs}}"`

- 每次保存文件时运行一个动作（默认为 `main`）：

`ghcid --run={{action}} {{path/to/Main.hs}}`

- 设置最大高度和宽度（默认为控制台的高度和宽度）：

`ghcid --height={{height}} --width={{width}} {{path/to/Main.hs}}`

- 将完整的 GHC 编译输出写入文件：

`ghcid --outputfile={{path/to/output_file.txt}} {{path/to/Main.hs}}`

- 每次保存文件时执行 REPL 命令（例如 `-- $> 1+1`）：

`ghcid --allow-eval {{path/to/Main.hs}}`