# cargo locate-project

> 打印项目的 `Cargo.toml` 清单的完整路径。
> 如果项目是工作区的一部分，则显示项目的清单，而不是工作区的。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>。

- 显示包含完整路径到 `Cargo.toml` 清单的 JSON 对象：

`cargo locate-project`

- 以指定格式显示项目路径：

`cargo locate-project --message-format {{plain|json}}`

- 显示位于工作区根目录而不是当前工作区成员的 `Cargo.toml` 清单：

`cargo locate-project --workspace`

- 显示特定目录中的 `Cargo.toml` 清单：

`cargo locate-project --manifest-path {{path/to/Cargo.toml}}`
