# cargo clippy

> 一组用于捕捉常见错误并提升你的 Rust 代码的 lint。
> 更多信息：<https://github.com/rust-lang/rust-clippy>。

- 对当前目录中的代码运行检查：

`cargo clippy`

- 要求 `Cargo.lock` 文件是最新的：

`cargo clippy --locked`

- 对工作区中的所有包运行检查：

`cargo clippy --workspace`

- 对某个包运行检查：

`cargo clippy --package {{package}}`

- 对某个 lint 组运行检查（见 <https://rust-lang.github.io/rust-clippy/stable/index.html#?groups=cargo,complexity,correctness,deprecated,nursery,pedantic,perf,restriction,style,suspicious>）：

`cargo clippy -- --warn clippy::{{lint_group}}`

- 将警告视为错误：

`cargo clippy -- --deny warnings`

- 运行检查并忽略警告：

`cargo clippy -- --allow warnings`

- 自动应用 Clippy 建议：

`cargo clippy --fix`