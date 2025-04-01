# rustup toolchain

> 管理 Rust 工具链。
> 有关工具链的更多信息，请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>。

- 安装或更新指定的工具链：

`rustup install {{toolchain}}`

- 卸载工具链：

`rustup uninstall {{toolchain}}`

- 列出已安装的工具链：

`rustup list`

- 通过符号链接创建自定义工具链：

`rustup link {{custom_toolchain_name}} {{path/to/directory}}`
