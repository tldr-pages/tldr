# cargo update

> 更新 `Cargo.lock` 中记录的依赖项。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-update.html>。

- 将 `Cargo.lock` 中的依赖项更新到最新可能的版本：

`cargo update`

- 显示将要更新的内容，但实际上不写入锁定文件：

`cargo update --dry-run`

- 仅更新指定的依赖项：

`cargo update --package {{dependency1}} --package {{dependency2}} --package {{dependency3}}`

- 将特定依赖项设置为特定版本：

`cargo update --package {{dependency}} --precise {{1.2.3}}`