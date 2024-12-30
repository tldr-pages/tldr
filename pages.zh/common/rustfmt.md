# rustfmt

> 格式化 Rust 源代码。
> 更多信息：<https://github.com/rust-lang/rustfmt>。

- 格式化一个文件，覆盖原文件：

`rustfmt {{path/to/source.rs}}`

- 检查一个文件的格式并在控制台上显示任何更改：

`rustfmt --check {{path/to/source.rs}}`

- 在格式化之前备份任何修改过的文件（原文件将被重命名为 `.bk` 扩展名）：

`rustfmt --backup {{path/to/source.rs}}`