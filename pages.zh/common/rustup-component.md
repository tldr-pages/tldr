# rustup 组件

> 修改工具链的已安装组件。
> 如果没有 `--toolchain` 选项，`rustup` 将使用默认工具链。有关工具链的更多信息，请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>。

- 向工具链添加组件：

`rustup component add --toolchain {{toolchain}} {{component}}`

- 从工具链中移除组件：

`rustup component remove --toolchain {{toolchain}} {{component}}`

- 列出工具链的已安装和可用组件：

`rustup component list --toolchain {{toolchain}}`

- 列出工具链的已安装组件：

`rustup component list --toolchain {{toolchain}} --installed`