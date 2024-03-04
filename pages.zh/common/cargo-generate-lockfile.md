# cargo generate-lockfile

> 为当前包生成 Cargo.lock 文件。类似于 cargo update，但选项更少。
> 如果锁定文件已经存在，它将使用每个包的最新版本重新构建。
> 更多信息：<https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>.

- 使用每个包的最新版本生成Cargo.lock文件：

`cargo generate-lockfile`
