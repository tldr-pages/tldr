# rustc

> Rust 编译器。
> Rust 项目通常使用 `cargo` 而不是直接调用 `rustc`。
> 更多信息请访问: <https://doc.rust-lang.org/rustc>。

- 编译一个二进制 crate:

`rustc {{path/to/main.rs}}`

- 使用优化编译（`s` 表示优化二进制大小；`z` 是更进一步的优化）:

`rustc -C lto -C opt-level={{0|1|2|3|s|z}} {{path/to/main.rs}}`

- 编译时包含调试信息:

`rustc -g {{path/to/main.rs}}`

- 解释错误信息:

`rustc --explain {{error_code}}`

- 针对当前 CPU 编译特定架构的优化:

`rustc -C target-cpu={{native}} {{path/to/main.rs}}`

- 显示目标列表（注意：您必须先使用 `rustup` 添加一个目标才能编译它）:

`rustc --print target-list`

- 针对特定目标编译:

`rustc --target {{target_triple}} {{path/to/main.rs}}`