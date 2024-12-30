# cargo 元数据

> 以 JSON 格式输出当前包的工作区成员和解析的依赖项。
> 注意：输出格式可能会在未来的 Cargo 版本中发生变化。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-metadata.html>。

- 打印当前包的工作区成员和解析的依赖项：

`cargo metadata`

- 仅打印工作区成员，不获取依赖项：

`cargo metadata --no-deps`

- 根据指定版本以特定格式打印元数据：

`cargo metadata --format-version {{version}}`

- 打印包含仅针对给定目标三元组的依赖项的 `resolve` 字段的元数据（注意：`packages` 数组仍将包括所有目标的依赖项）：

`cargo metadata --filter-platform {{target_triple}}`