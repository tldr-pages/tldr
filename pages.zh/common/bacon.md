# bacon

> Rust 的后台代码检查器。
> 更多信息：<https://github.com/Canop/bacon>。

- 在当前目录检测到更改时运行 `cargo check`：

`bacon`

- 在给定目录检测到更改时运行 `cargo test`：

`bacon test {{路径/到/目录}}`

- 在当前目录检测到更改时针对所有目标运行 `cargo check`：

`bacon check-all`

- 在当前目录检测到更改时运行特定任务：

`bacon {{run|test|clippy|doc|...}}`

- 列出所有当前可用的任务：

`bacon --list-jobs`

- 在当前目录初始化 `bacon.toml` 配置文件：

`bacon --init`
