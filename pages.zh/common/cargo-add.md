# cargo add

> 向 Rust 项目的 `Cargo.toml` 文件添加依赖项。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- 将最新版本的依赖项添加到当前项目：

`cargo add {{依赖项}}`

- 添加特定版本的依赖项：

`cargo add {{依赖项}}@{{版本号}}`

- 添加依赖项并启动一个或多个特定功能：

`cargo add {{依赖项}} --features {{功能1}},{{功能2}}`

- 添加一个可选的依赖项，然后将其作为包(crate)的一个功能暴露出来：

`cargo add {{依赖项}} --optional`

- 将本地包(crate)添加为依赖项：

`cargo add --path {{path/to/directory}}`

- 添加一个开发或构建依赖项：

`cargo add {{依赖项}} --{{dev|build}}`

- 添加一个禁用所有默认功能的依赖项：

`cargo add {{依赖项}} --no-default-features`
