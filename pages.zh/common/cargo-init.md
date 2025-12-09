# cargo init

> 创建一个新的 Cargo 包。
> 相当于 `cargo new`，但是指定目录是可选的。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- 在当前目录中初始化一个带有二进制目标的 Rust 项目：

`cargo init`

- 在指定目录中初始化一个带有二进制目标的 Rust 项目：

`cargo init {{path/to/directory}}`

- 在当前目录中初始化一个带有库目标的 Rust 项目：

`cargo init --lib`

- 在项目目录中初始化版本控制系统仓库 (默认为git)：

`cargo init --vcs {{git|hg|pijul|fossil|none}}`

- 设置包名称 (默认为目录名称)：

`cargo init --name {{name}}`
