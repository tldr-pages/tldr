# rustdoc

> 为 Rust 项目生成文档。
> 更多信息：<https://doc.rust-lang.org/stable/rustdoc>。

- 从项目的根文件生成文档：

`rustdoc {{src/lib.rs}}`

- 为项目指定一个名称：

`rustdoc {{src/lib.rs}} --crate-name {{name}}`

- 从 Markdown 文件生成文档：

`rustdoc {{path/to/file.md}}`

- 指定输出目录：

`rustdoc {{src/lib.rs}} --out-dir {{path/to/output_directory}}`
