# rustup 哪个

> 显示将为由 `rustup` 管理的命令运行的二进制文件。
> 类似于 `which`，但搜索的是 Rust 工具链而不是 `$PATH`。
> 更多信息：<https://rust-lang.github.io/rustup>。

- 显示默认工具链中二进制文件的路径：

`rustup 哪个 {{command}}`

- 显示指定工具链中二进制文件的路径（更多信息请参见 `rustup help toolchain`）：

`rustup 哪个 --toolchain {{toolchain}} {{command}}`