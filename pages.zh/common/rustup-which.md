# rustup which

> 显示 `rustup` 管理的命令将运行哪个二进制文件。
> 类似 `which` 命令，但搜索的是 Rust 工具链而不是 `$PATH`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 显示默认工具链中命令的二进制文件路径：

`rustup which {{命令}}`

- 显示指定工具链中命令的二进制文件路径（有关工具链的更多信息，请参见 `rustup help toolchain`）：

`rustup which --toolchain {{工具链}} {{命令}}`
