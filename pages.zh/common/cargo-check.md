# cargo check

> 检查本地包及其所有依赖项是否存在错误。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-check.html>。

- 检查当前包：

`cargo check`

- 检查所有测试：

`cargo check --tests`

- 检查 `tests/integration_test1.rs` 中的集成测试：

`cargo check --test {{integration_test1}}`

- 检查当前包并启用特性 `feature1` 和 `feature2`：

`cargo check --features {{feature1,feature2}}`

- 检查当前包并禁用默认特性：

`cargo check --no-default-features`