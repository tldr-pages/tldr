# cargo

> 管理 Rust 项目及其模块依赖（crate）。
> 一些子命令如 `build` 有自己的使用文档。
> 更多信息：<https://doc.rust-lang.org/cargo>。

- 搜索 crates：

`cargo search {{search_string}}`

- 安装一个二进制 crate：

`cargo install {{crate_name}}`

- 列出已安装的二进制 crates：

`cargo install --list`

- 在指定目录（默认是当前工作目录）中创建一个新的二进制或库 Rust 项目：

`cargo init --{{bin|lib}} {{path/to/directory}}`

- 向当前目录中的 `Cargo.toml` 添加一个依赖：

`cargo add {{dependency}}`

- 使用发布配置构建当前目录中的 Rust 项目：

`cargo build --release`

- 使用 nightly 编译器构建当前目录中的 Rust 项目（需要 `rustup`）：

`cargo +nightly build`

- 使用特定线程数构建（默认是逻辑 CPU 的数量）：

`cargo build --jobs {{number_of_threads}}`