# cargo rustdoc

> 构建 Rust 包的文档。
> 类似于 `cargo doc`，但您可以传递选项给 `rustdoc`。有关所有可用选项，请参见 `rustdoc --help`。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>。

- 传递选项给 `rustdoc`：

`cargo rustdoc -- {{rustdoc_options}}`

- 对文档 lint 发出警告：

`cargo rustdoc -- --warn rustdoc::{{lint_name}}`

- 忽略文档 lint：

`cargo rustdoc -- --allow rustdoc::{{lint_name}}`

- 文档包的库：

`cargo rustdoc --lib`

- 文档指定的二进制文件：

`cargo rustdoc --bin {{name}}`

- 文档指定的示例：

`cargo rustdoc --example {{name}}`

- 文档指定的集成测试：

`cargo rustdoc --test {{name}}`