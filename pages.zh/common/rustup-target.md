# rustup target

> 修改工具链支持的目标平台。
> 如果不使用 `--toolchain` 选项，`rustup` 会使用默认工具链。更多信息请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 为工具链添加目标平台：

`rustup target add --toolchain {{工具链}} {{目标}}`

- 从工具链移除目标平台：

`rustup target remove --toolchain {{工具链}} {{目标}}`

- 列出工具链的可用目标平台和已安装目标平台：

`rustup target list --toolchain {{工具链}}`

- 列出工具链已安装的目标平台：

`rustup target list --toolchain {{工具链}} --installed`
