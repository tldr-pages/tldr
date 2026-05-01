# rustc

> Rust 编译器。
> Rust 项目通常使用 `cargo` 而不是直接调用 `rustc`。
> 更多信息：<https://doc.rust-lang.org/stable/rustc/>。

- 编译二进制包（crate）：

`rustc {{路径/到/主文件.rs}}`

- 编译时启用优化（`s` 表示针对二进制大小优化；`z` 含义相同但使用更多优化）：

`rustc {{[-C|--codegen]}} lto {{[-C|--codegen]}} opt-level={{0|1|2|3|s|z}} {{路径/到/主文件.rs}}`

- 编译时包含调试信息：

`rustc {{[-g|--codegen debuginfo=2]}} {{路径/到/主文件.rs}}`

- 解释错误信息：

`rustc --explain {{错误码}}`

- 编译时针对当前 CPU 架构启用特定优化：

`rustc {{[-C|--codegen]}} target-cpu={{native}} {{路径/到/主文件.rs}}`

- 显示目标列表（注意：你必须先使用 `rustup` 添加目标才能为其编译）：

`rustc --print target-list`

- 针对特定目标编译：

`rustc --target {{目标三元组}} {{路径/到/主文件.rs}}`

- 显示帮助：

`rustc {{[-h|--help]}}`
