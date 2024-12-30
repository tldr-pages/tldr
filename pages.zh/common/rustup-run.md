# rustup 运行

> 使用配置好的 Rust 工具链环境运行命令。
> 注意：所有由 `rustup` 管理的命令都有一个简写方式：例如，`cargo +nightly build` 相当于 `rustup run nightly cargo build`。
> 更多信息：<https://rust-lang.github.io/rustup>。

- 使用给定的 Rust 工具链运行命令（有关更多信息，请参见 `rustup help toolchain`）：

`rustup run {{toolchain}} {{command}}`