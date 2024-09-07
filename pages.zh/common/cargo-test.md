# cargo test

> 执行 Rust 包的单元测试和集成测试。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- 仅运行包含特定字符串在其名称中的测试：

`cargo test {{测试名称}}`

- 设置并行运行测试用例的数量：

`cargo test -- --test-threads {{数量}}`

- 在 release 模式下测试构建，启用优化：

`cargo test --release`

- 测试工作区中的所有包：

`cargo test --workspace`

- 为特定包运行测试：

`cargo test --package {{包名}}`

- 运行测试时不隐藏测试执行的输出：

`cargo test -- --nocapture`
