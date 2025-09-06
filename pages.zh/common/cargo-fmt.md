# cargo fmt

> 在 Rust 项目中对所有源文件运行 `rustfmt`。
> 更多信息：<https://github.com/rust-lang/rustfmt>.

- 格式化所有源文件：

`cargo fmt`

- 检查格式错误，不对文件进行写入操作：

`cargo fmt --check`

- 将参数传递给每个 rustfmt 调用：

`cargo fmt -- {{rustfmt参数}}`
