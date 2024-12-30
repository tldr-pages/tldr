# cargo 生成锁定文件

> 为当前包生成 `Cargo.lock` 文件。类似于 `cargo update`，但选项较少。
> 如果锁定文件已存在，将使用每个包的最新版本重新构建。
> 更多信息：<https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>。

- 生成一个包含每个包最新版本的 `Cargo.lock` 文件：

`cargo generate-lockfile`