# rustup-init.sh

> 用于安装 `rustup` 和 Rust 工具链的脚本。
> 更多信息：<https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- 下载并运行 `rustup-init` 来安装 `rustup` 和默认 Rust 工具链：

`curl https://sh.rustup.rs {{[-sSf|--silent --show-error --fail]}} | sh -s`

- 下载并运行 `rustup-init` 并传递参数：

`curl https://sh.rustup.rs {{[-sSf|--silent --show-error --fail]}} | sh -s -- {{参数}}`

- 运行 `rustup-init` 并指定要安装的额外组件或目标：

`rustup-init.sh --target {{目标}} --component {{组件}}`

- 运行 `rustup-init` 并指定要安装的默认工具链：

`rustup-init.sh --default-toolchain {{工具链}}`

- 运行 `rustup-init` 并不安装任何工具链：

`rustup-init.sh --default-toolchain {{none}}`

- 运行 `rustup-init` 并指定安装配置文件：

`rustup-init.sh --profile {{minimal|default|complete}}`

- 运行 `rustup-init` 并跳过确认提示：

`rustup-init.sh -y`
