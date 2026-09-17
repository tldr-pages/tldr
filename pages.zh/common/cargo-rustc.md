# cargo rustc

> 编译一个 Rust 软件包。类似于 `cargo build`，但您可以向编译器传递额外的选项。
> 查看 `rustc --help` 获取所有可用选项。
> 另请参阅：`rustc`。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>。

- 构建软件包并向 `rustc` 传递选项：

`cargo rustc -- {{rustc_options}}`

- 在 release 模式下构建，启用优化：

`cargo rustc {{[-r|--release]}}`

- 使用针对当前 CPU 的特定架构优化编译：

`cargo rustc {{[-r|--release]}} -- {{[-C|--codegen]}} target-cpu=native`

- 使用速度优化编译：

`cargo rustc -- {{[-C|--codegen]}} opt-level={{1|2|3}}`

- 使用体积（[s]ize）优化编译（`z` 也会关闭循环向量化）：

`cargo rustc -- {{[-C|--codegen]}} opt-level={{s|z}}`

- 检查您的软件包是否使用了不安全的代码：

`cargo rustc --lib -- -D unsafe-code`

- 构建特定的软件包：

`cargo rustc {{[-p|--package]}} {{软件包}}`

- 仅构建指定的二进制文件：

`cargo rustc --bin {{名称}}`
