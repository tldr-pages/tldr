# cargo fmt

> 在Rust项目的所有源文件上运行`rustfmt`。
> 更多信息：<https://github.com/rust-lang/rustfmt>。

- 格式化所有源文件：

`cargo fmt`

- 检查格式化错误而不写入文件：

`cargo fmt --check`

- 将参数传递给每个`rustfmt`调用：

`cargo fmt -- {{rustfmt_args}}`