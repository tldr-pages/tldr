# rustup toolchain

> 管理 Rust 工具链。
> 有关工具链的更多信息，请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 安装或更新指定工具链：

`rustup toolchain install {{工具链}}`

- 卸载工具链：

`rustup toolchain uninstall {{工具链}}`

- 列出已安装的工具链：

`rustup toolchain list`

- 通过创建符号链接来创建自定义工具链：

`rustup toolchain link {{自定义工具链名称}} {{path/to/directory}}`
