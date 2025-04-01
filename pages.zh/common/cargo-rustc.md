# cargo rustc

> 编译一个 Rust 包。类似于 `cargo build`，但您可以向编译器传递额外的选项。
> 查看 `rustc --help` 获取所有可用选项。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- 构建包并向 `rustc` 传递选项：

`cargo rustc -- {{rustc_options}}`

- 在 release 模式下构建构建，启用优化：

`cargo rustc --release`

- 使用针对当前 CPU 的特定架构优化编译：

`cargo rustc --release -- -C target-cpu=native`

- 使用速度优化编译：

`cargo rustc -- -C opt-level {{1|2|3}}`

- 使用 [s]ize 优化编译（`z` 也会关闭循环向量化）：

`cargo rustc -- -C opt-level {{s|z}}`

- 检查您的包是否使用了不安全的代码：

`cargo rustc --lib -- -D unsafe-code`

- 构建特定的包：

`cargo rustc --package {{package}}`

- 仅构建指定的二进制文件：

`cargo --bin {{名称}}`
