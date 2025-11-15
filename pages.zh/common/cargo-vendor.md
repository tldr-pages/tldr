# cargo vendor

> 将项目的所有依赖项存储到指定目录中（默认为 `vendor`）。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-vendor.html>.

- 将依赖项存储到指定目录，并配置在当前项目中使用这些存储的源代码：

`cargo vendor {{path/to/directory}} > .cargo/config.toml`
