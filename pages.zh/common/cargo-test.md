# cargo test

> 执行 Rust 包的单元测试和集成测试。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-test.html>。

- 仅运行名称中包含特定字符串的测试：

`cargo test {{testname}}`

- 设置同时运行的测试用例数量：

`cargo test -- --test-threads {{count}}`

- 在发布模式下测试，带有优化：

`cargo test --release`

- 测试工作区中的所有包：

`cargo test --workspace`

- 运行特定包的测试：

`cargo test --package {{package}}`

- 运行测试时不隐藏测试执行的输出：

`cargo test -- --nocapture`