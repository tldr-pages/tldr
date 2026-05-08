# rustdoc

> 为 Rust 包（crate）生成文档。
> 更多信息：<https://doc.rust-lang.org/stable/rustdoc/>。

- 从包（crate）的根文件生成文档：

`rustdoc {{src/lib.rs}}`

- 为项目传递一个名称：

`rustdoc {{src/lib.rs}} --crate-name {{名称}}`

- 从 Markdown 文件生成文档：

`rustdoc {{路径/到/文件.md}}`

- 指定输出目录：

`rustdoc {{src/lib.rs}} {{[-o|--out-dir]}} {{路径/到/输出目录}}`

- 显示帮助：

`rustdoc {{[-h|--help]}}`
