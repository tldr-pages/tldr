# cargo add

> 向 Rust 项目的 `Cargo.toml` 清单添加依赖项。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-add.html>。

- 向当前项目添加依赖项的最新版本：

`cargo add {{dependency}}`

- 添加特定版本的依赖项：

`cargo add {{dependency}}@{{version}}`

- 添加依赖项并启用一个或多个特定功能：

`cargo add {{dependency}} --features {{feature_1}},{{feature_2}}`

- 添加一个可选依赖项，该依赖项将作为 crate 的一个功能暴露：

`cargo add {{dependency}} --optional`

- 将本地 crate 添加为依赖项：

`cargo add --path {{path/to/crate_directory}}`

- 添加开发或构建依赖项：

`cargo add {{dependency}} --{{dev|build}}`

- 添加禁用所有默认功能的依赖项：

`cargo add {{dependency}} --no-default-features`