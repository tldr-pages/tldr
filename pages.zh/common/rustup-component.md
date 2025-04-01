# rustup component

> 修改工具链已安装的组件。
> 如果没有使用 `--toolchain` 选项，`rustup` 将使用默认工具链。有关工具链的更多信息，请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 向工具链添加组件：

`rustup component add --toolchain {{toolchain}} {{component}}`

- 从工具链中删除组件：

`rustup component remove --toolchain {{toolchain}} {{component}}`

- 列出工具链已安装和可用的组件：

`rustup component list --toolchain {{toolchain}}`

- 列出工具链已安装的组件：

`rustup component list --toolchain {{toolchain}} --installed`