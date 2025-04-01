# rustup target

> 修改工具链支持的目标。
> 不使用 `--toolchain` 选项时，`rustup` 将使用默认工具链。有关工具链的更多信息，请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 向工具链添加目标：

`rustup target add --toolchain {{toolchain}} {{target}}`

- 从工具链中移除目标：

`rustup target remove --toolchain {{toolchain}} {{target}}`

- 列出工具链支持的可用和已安装目标：

`rustup target list --toolchain {{toolchain}}`

- 列出工具链已安装的目标：

`rustup target list --toolchain {{toolchain}} --installed`
