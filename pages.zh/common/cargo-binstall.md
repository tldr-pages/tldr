# cargo binstall

> 从 CI 产物安装 Rust 二进制文件。
> 如果没有可用的二进制文件，则回退到 `cargo install`（从源代码安装）。
> 更多信息：<https://github.com/cargo-bins/cargo-binstall>。

- 从 <https://crates.io> 安装一个包：

`cargo binstall {{包名}}`

- 安装指定版本的包（默认为最新版本）：

`cargo binstall {{包名}}@{{版本号}}`

- 安装包并禁用确认提示：

`cargo binstall {{[-y|--no-confirm]}} {{包名}}`
