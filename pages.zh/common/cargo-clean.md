# cargo clean

> 删除 `target` 目录中的生成的工件。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-clean.html>。

- 删除整个 `target` 目录：

`cargo clean`

- 删除文档工件（`target/doc` 目录）：

`cargo clean --doc`

- 删除发布工件（`target/release` 目录）：

`cargo clean --release`

- 删除给定配置文件目录中的工件（在这种情况下为 `target/debug`）：

`cargo clean --profile {{dev}}`