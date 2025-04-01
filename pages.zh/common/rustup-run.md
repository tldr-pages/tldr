# rustup run

> 使用配置了 Rust 工具链的环境运行命令。
> 注意：所有由 `rustup` 管理的命令都有一个简写形式：例如，`cargo +nightly build` 等同于 `rustup run nightly cargo build`。
> 更多信息：<https://rust-lang.github.io/rustup>。

- 使用指定的 Rust 工具链运行命令（关于 `rustup help toolchain` 的更多信息，请参阅 `rustup help toolchain`）：

`rustup run {{toolchain}} {{command}}`