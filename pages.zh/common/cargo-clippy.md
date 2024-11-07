# cargo clippy

> 一系列 lint 工具，用于捕获常见错误并改进 Rust 代码。
> 更多信息：<https://github.com/rust-lang/rust-clippy>.

- 对当前目录中的代码运行检查：

`cargo clippy`

- 要求 `Cargo.lock` 文件是最新的：

`cargo clippy --locked`

- 对工作区中的所有包进行检查：

`cargo clippy --workspace`

- 对某个包进行检查：

`cargo clippy --package {{包名}}`

- 运行特定 lint 组的检查（参见 <https://rust-lang.github.io/rust-clippy/stable/index.html#?groups=cargo,complexity,correctness,deprecated,nursery,pedantic,perf,restriction,style,suspicious>）：

`cargo clippy -- --warn clippy::{{lint组}}`

- 将警告视为错误：

`cargo clippy -- --deny warnings`

- 运行检查并忽略警告：

`cargo clippy -- --allow warnings`

- 自动应用 Clippy 的建议：

`cargo clippy --fix`
