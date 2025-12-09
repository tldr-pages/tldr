# cargo remove

> 从 Rust 项目的 `Cargo.toml` 清单中移除依赖关系。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- 从当前项目中移除一个依赖项：

`cargo remove {{依赖项}}`

- 移除开发或构建依赖项：

`cargo remove --{{dev|build}} {{依赖项}}`

- 移除给定目标平台的依赖项：

`cargo remove --target {{目标平台}} {{依赖项}}`
