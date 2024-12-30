# cargo rustc

> 编译一个 Rust 包。类似于 `cargo build`，但您可以向编译器传递额外的选项。
> 有关所有可用选项，请参阅 `rustc --help`。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>。

- 构建包并将选项传递给 `rustc`：

`cargo rustc -- {{rustc_options}}`

- 以发布模式构建工件，并进行优化：

`cargo rustc --release`

- 针对当前 CPU 进行架构特定的优化编译：

`cargo rustc --release -- -C target-cpu=native`

- 进行速度优化编译：

`cargo rustc -- -C opt-level {{1|2|3}}`

- 进行 [s]ize 优化编译（`z` 也会关闭循环向量化）：

`cargo rustc -- -C opt-level {{s|z}}`

- 检查您的包是否使用了不安全代码：

`cargo rustc --lib -- -D unsafe-code`

- 构建特定的包：

`cargo rustc --package {{package}}`

- 仅构建指定的二进制文件：

`cargo --bin {{name}}`