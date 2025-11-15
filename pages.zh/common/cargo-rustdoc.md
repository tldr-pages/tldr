# cargo rustdoc

> 构建 Rust 包的文档。
> 类似于 `cargo doc`，但您可以向 `rustdoc` 传递选项。查看 `rustdoc --help` 获取所有可用选项。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- 向 `rustdoc` 传递选项：

`cargo rustdoc -- {{rustdoc_options}}`

- 关于文档 lint 发出警告：

`cargo rustdoc -- --warn rustdoc::{{lint_name}}`

- 忽略文档 lint:

`cargo rustdoc -- --allow rustdoc::{{lint_name}}`

- 为包的库生成文档：

`cargo rustdoc --lib`

- 为指定的二进制文件生成文档：

`cargo rustdoc --bin {{名称}}`

- 为指定的示例生成文档：

`cargo rustdoc --example {{名称}}`

- 为指定的集成测试生成文档：

`cargo rustdoc --test {{名称}}`
