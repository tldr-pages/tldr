# cargo vendor

> 将项目的所有依赖项放入指定目录（默认为 `vendor`）。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-vendor.html>。

- 供应依赖项并配置 `cargo` 使用当前项目中的供应源：

`cargo vendor {{path/to/directory}} > .cargo/config.toml`