# cargo

> 管理 Rust 项目及其模块依赖项（crates）。
> 此命令也有关于其子命令的文件，例如：`build`.
> 更多信息：<https://doc.rust-lang.org/stable/cargo/>。

- 搜索包：

`cargo search {{搜索关键词}}`

- 安装二进制包（crate）：

`cargo install {{包名}}`

- 列出已安装的二进制包（crate）：

`cargo install --list`

- 在指定目录（或默认情况下在当前工作目录）中创建一个新的二进制或库 Rust 项目：

`cargo init --{{bin|lib}} {{路径/到/目录}}`

- 向当前目录的 `Cargo.toml` 添加一个依赖：

`cargo add {{依赖项目}}`

- 使用 release 模式在当前目录中构建 Rust 项目：

`cargo {{[b|build]}} {{[-r|--release]}}`

- 使用最新的编译器在当前目录中构建 Rust 项目（需要 `rustup`）：

`cargo +nightly {{[b|build]}}`

- 使用特定数量的线程构建（默认为逻辑 CPU 的数量）：

`cargo {{[b|build]}} {{[-j|--jobs]}} {{线程数}}`
