# rustup-init.sh

> 安装 `rustup` 和 Rust 工具链的脚本。
> 更多信息：<https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>。

- 下载并运行 `rustup-init` 以安装 `rustup` 和默认的 Rust 工具链：

`curl https://sh.rustup.rs -sSf | sh -s`

- 下载并运行 `rustup-init` 并传递参数：

`curl https://sh.rustup.rs -sSf | sh -s -- {{arguments}}`

- 运行 `rustup-init` 并指定要安装的附加组件或目标：

`rustup-init.sh --target {{target}} --component {{component}}`

- 运行 `rustup-init` 并指定要安装的默认工具链：

`rustup-init.sh --default-toolchain {{toolchain}}`

- 运行 `rustup-init` 并不安装任何工具链：

`rustup-init.sh --default-toolchain {{none}}`

- 运行 `rustup-init` 并指定安装配置文件：

`rustup-init.sh --profile {{minimal|default|complete}}`

- 运行 `rustup-init` 时不询问确认：

`rustup-init.sh -y`