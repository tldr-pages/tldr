# rustc

> Rust 编译器。
> Rust 项目通常使用 `cargo` 而不是直接调用 `rustc`。
> 更多信息：<https://doc.rust-lang.org/rustc>。

- 编译一个二进制 crate：

`rustc {{path/to/main.rs}}`

- 使用优化编译 (`s` 表示优化二进制文件大小；`z` 表示更高级别的优化)：

`rustc -C lto -C opt-level={{0|1|2|3|s|z}} {{path/to/main.rs}}`

- 使用调试信息编译：

`rustc -g {{path/to/main.rs}}`

- 解释错误信息：

`rustc --explain {{error_code}}`

- 使用当前 CPU 的架构特性进行优化编译：

`rustc -C target-cpu={{native}} {{path/to/main.rs}}`

- 显示目标列表（注意：需要先使用 `rustup` 添加目标才能进行编译）：

`rustc --print target-list`

- 为特定目标编译：

`rustc --target {{target_triple}} {{path/to/main.rs}}`
