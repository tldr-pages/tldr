# cargo update

> 更新记录在 `Cargo.lock` 中的依赖关系。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-update.html>.

- 将 `Cargo.lock` 中的依赖项更新为可能的最新版本：

`cargo update`

- 显示将会更新的内容，但实际上不写入锁定文件：

`cargo update --dry-run`

- 仅更新指定的依赖项：

`cargo update --package {{依赖项1}} --package {{依赖项2}} --package {{依赖项3}}`

- 将特定依赖项设置为特定版本：

`cargo update --package {{依赖项}} --precise {{1.2.3}}`
