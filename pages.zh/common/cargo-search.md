# cargo 搜索

> 在 <https://crates.io> 上搜索包。
> 这些包将以适合复制到 `Cargo.toml` 的 TOML 格式显示，并附有描述。
> 更多信息： <https://doc.rust-lang.org/cargo/commands/cargo-search.html>。

- 搜索包：

`cargo search {{query}}`

- 显示 `n` 个结果（默认：10，最大：100）：

`cargo search --limit {{n}} {{query}}`