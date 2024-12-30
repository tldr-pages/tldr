# cargo publish

> 将一个包上传到注册表。
> 注意：在发布包之前，您必须使用 `cargo login` 添加身份验证令牌。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-publish.html>。

- 执行检查，创建一个 `.crate` 文件并将其上传到注册表：

`cargo publish`

- 执行检查，创建一个 `.crate` 文件但不上传（相当于 `cargo package`）：

`cargo publish --dry-run`

- 使用指定的注册表（注册表名称可以在配置中定义 - 默认是 <https://crates.io>）：

`cargo publish --registry {{name}}`