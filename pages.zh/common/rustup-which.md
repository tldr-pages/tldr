# rustup which

> 显示 `rustup` 管理的命令将运行的可执行文件路径。
> 类似于 `which`，但搜索的是 Rust 工具链而不是 `$PATH`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 显示默认工具链中命令的可执行文件路径：

`rustup which {{command}}`

- 显示指定工具链中命令的可执行文件路径（更多关于工具链的信息，请参阅 `rustup help toolchain`）：

`rustup which --toolchain {{toolchain}} {{command}}`