# cargo remove

> 从 Rust 项目的 `Cargo.toml` 清单中移除依赖。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-remove.html>。

- 从当前项目中移除一个依赖：

`cargo remove {{dependency}}`

- 移除一个开发或构建依赖：

`cargo remove --{{dev|build}} {{dependency}}`

- 移除给定目标平台的依赖：

`cargo remove --target {{target}} {{dependency}}`