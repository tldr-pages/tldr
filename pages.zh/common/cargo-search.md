# cargo search

> 在 https://crates.io 上搜索包。
> 显示包及其描述，以 TOML 格式显示，可复制到 `Cargo.toml` 中。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-search.html>.

- 搜索包：

`cargo search {{查询词}}`

- 显示 n 个结果 (默认为 10，最多为 100)：

`cargo search --limit {{n}} {{查询词}}`
