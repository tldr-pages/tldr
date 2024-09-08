# cargo check

> 检查本地软件包及其所有依赖包是否有错误。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-check.html>.

- 检查当前包：

`cargo check`

- 检查所有测试：

`cargo check --tests`

- 检查 `tests/integration_test1.rs` 中的集成测试：

`cargo check --test {{integration_test1}}`

- 使用 `feature1` 和 `feature2` 功能检查当前包：

`cargo check --features {{feature1,feature2}}`

- 禁用默认功能后检测当前包：

`cargo check --no-default-features`
