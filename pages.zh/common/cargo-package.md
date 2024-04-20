# cargo package

> 将本地包装成一个可分发的 tarball 文件（`.crate` 文件）。
> 类似于 `cargo publish --dry-run`，但具有更多选项。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-package.html>.

- 执行检查并创建一个 `.crate` 文件 (相当于 `cargo publish --dry-run`)：

`cargo package`

- 显示将包含在tarball中的文件，而不实际创建它：

`cargo package --list`
