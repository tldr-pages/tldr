# rustup component

> 修改已安装工具链的组件。
> 如果不使用 `--toolchain` 选项，`rustup` 将使用默认工具链。有关工具链的更多信息请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 向工具链添加组件：

`rustup component add --toolchain {{工具链}} {{组件}}`

- 从工具链中移除组件：

`rustup component remove --toolchain {{工具链}} {{组件}}`

- 列出工具链已安装和可用的组件：

`rustup component list --toolchain {{工具链}}`

- 列出工具链已安装的组件：

`rustup component list --toolchain {{工具链}} --installed`
