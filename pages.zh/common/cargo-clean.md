# cargo clean

> 删除 `target` 目录中生成的构建产物。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-clean.html>.

- 删除整个 `target` 目录：

`cargo clean`

- 删除文档构建产物 (`target/doc` 目录)：

`cargo clean --doc`

- 删除 release 模式的构建产物 (`target/release` 目录)：

`cargo clean --release`

- 删除给定配置文件的目录中的构建产物（在本例中为 `target/debug`)：

`cargo clean --profile {{dev}}`
