# bacon

> 用于 Rust 的后台代码检查工具。
> 更多信息：<https://github.com/Canop/bacon>。

- 当当前目录中的文件发生变化时，运行 `cargo check`：

`bacon`

- 当指定目录中的文件发生变化时，运行 `cargo test`：

`bacon test {{path/to/directory}}`

- 当当前目录中的文件发生变化时，对所有目标运行 `cargo check`：

`bacon check-all`

- 当当前目录中的文件发生变化时，运行指定的任务：

`bacon {{run|test|clippy|doc|...}}`

- 列出所有可用的任务：

`bacon --list-jobs`

- 在当前目录中初始化一个 `bacon.toml` 配置文件：

`bacon --init`
