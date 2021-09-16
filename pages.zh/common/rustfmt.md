# rustfmt

> 格式化 Rust 源代码的工具。
> 更多信息：<https://github.com/rust-lang/rustfmt>.

- 格式化文件，就地覆盖原始文件：

`rustfmt {{source.rs}}`

- 检查文件的格式并在控制台上显示所有更改：

`rustfmt --check {{source.rs}}`

- 格式化之前，备份所有修改过的文件（原始文件的扩展名为 `.bk`）：

`rustfmt --backup {{source.rs}}`
